# Prompt 04: LTR APA 7th Edition Bibliography & Clickable Author-Year Citations

## Engineering Context
- **Stage:** Bibliography Modernization & Academic Compliance
- **Trigger:** Default `\bibliographystyle{plain}` rendered right-to-left with numbered `[1]` labels on the right, misplaced periods, Title Case entries, and publisher city/state fields violating APA 7th edition.

## Collaborative Dispatch Prompt Used
```text
In the bibliography section, the text is currently aligned right-to-left. Update it so that it is aligned and written left-to-right (LTR), ensuring it is formatted correctly and accurately according to the latest APA 7th edition guidelines, and review the changes together across all agents:

- theory: Audit all 24 entries in references.bib for full APA 7th compliance (sentence-case titles, inverted Surname F. M. for all authors, serial comma + &, italicized journals/volumes + attached non-italic issue, Article eabo6254 for Science Advances, removal of publisher city/state, full https://doi.org/... and EUR-Lex URLs without trailing periods, and APA 7th Chapter 11 legal case & statute formatting).
- architect: Design the cleanest LuaLaTeX + babel(bidi=basic) LTR bibliography layout with 0.5-inch hanging indents and RTL Hebrew chapter heading ("ביבליוגרפיה (References)").
- redteam: Audit URL/DOI line wrapping, BiDi isolation of parenthetical in-text citations inside Hebrew prose, and zero Overfull hbox warnings.
- simulator: Confirm no regressions in Chapter 4 references/layout.
```

## Technical Adaptation (Post-Mortem #5)
- MiKTeX lacked `logreq.sty` / `biblatex-apa` (causing `biblatex` to hang in non-interactive mode). We implemented a zero-dependency native LuaLaTeX APA 7th engine in `civicshield.cls` (`apabibliography` canonical hanging-indent `list` with `\leftmargin=0.5in`, `\itemindent=-0.5in`, clickable `\hyperlink`/`\hypertarget` LTR parenthetical `\cite{...}`) paired with `chapters/references_apa7.tex` synced 1:1 with `references.bib`.
- Unanimously approved (`APPROVE`) by all 4 agents after visual verification of rendered pages 10, 34, 39, and 40.
