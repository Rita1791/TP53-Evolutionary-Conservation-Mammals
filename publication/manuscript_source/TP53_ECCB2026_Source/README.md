# OUP / ECCB Proceedings LaTeX Project

This folder contains the production-ready LaTeX project prepared for the ECCB Proceedings / OUP Bioinformatics template.

## Main files
- `main.tex`: main manuscript source
- `references.bib`: BibTeX bibliography database
- `main.bbl`: compiled bibliography snapshot for reproducible Overleaf compilation
- `oup-authoring-template.cls`: official OUP class file
- `oup-abbrvnat.bst`: OUP author-year bibliography style
- `oup-plain.bst`: OUP numbered bibliography style, retained from the official template
- `Fig/`: manuscript and supplementary figure files
- `supplementary.tex`: supplementary material source

## Recommended Overleaf compile settings
- Compiler: pdfLaTeX
- Bibliography: BibTeX
- Main document: `main.tex`

## Production checks performed
- Main manuscript compiles successfully with pdfLaTeX + BibTeX.
- Manuscript PDF is 7 pages.
- Abstract is 190 words, under the 250-word ECCB limit.
- Approximate extracted manuscript word count is 4,379 words, under the ~5,000-word guidance.
- OUP two-column formatting is retained.
- Citation formatting has been corrected to OUP author-year format.
- Figures are embedded and placed near first discussion in the results section.
- Author metadata, corresponding author, data/code availability, funding, author contributions, competing interests, ethics and acknowledgements are included.
