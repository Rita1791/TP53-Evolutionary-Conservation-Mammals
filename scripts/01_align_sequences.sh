#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:-data/processed/TP53_curated.fasta}"
OUTPUT="${2:-data/processed/TP53_aligned.fasta}"

if ! command -v mafft >/dev/null 2>&1; then
  echo "ERROR: MAFFT is not installed." >&2
  exit 127
fi

if [ ! -s "$INPUT" ]; then
  echo "ERROR: input FASTA not found or empty: $INPUT" >&2
  exit 2
fi

mkdir -p -- "$(dirname "$OUTPUT")" results/provenance

mafft --version 2> results/provenance/mafft_version.txt || true
mafft --auto --thread 1 --reorder "$INPUT" > "$OUTPUT"

python - "$OUTPUT" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
sequences = []
current = []
for raw in path.read_text(encoding="utf-8").splitlines():
    line = raw.strip()
    if line.startswith(">"):
        if current:
            sequences.append("".join(current))
        current = []
    elif line:
        current.append(line)
if current:
    sequences.append("".join(current))

if not sequences:
    raise SystemExit("ERROR: alignment contains no sequences")
lengths = {len(sequence) for sequence in sequences}
if len(lengths) != 1:
    raise SystemExit(f"ERROR: alignment lengths differ: {sorted(lengths)}")
print(f"Validated {len(sequences)} aligned sequences; length={lengths.pop()}")
PY

sha256sum "$INPUT" "$OUTPUT" > results/provenance/alignment_checksums.sha256
echo "Alignment written to: $OUTPUT"

