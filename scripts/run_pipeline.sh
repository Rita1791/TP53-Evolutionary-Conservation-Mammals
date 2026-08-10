#!/usr/bin/env bash
set -euo pipefail

bash scripts/01_align_sequences.sh
python scripts/conservation_analysis.py
python scripts/hotspot_analysis.py
python scripts/mutation_analysis.py
python scripts/permutation_analysis.py --iterations 100000 --seed 42

echo "TP53 mammalian analysis completed."

