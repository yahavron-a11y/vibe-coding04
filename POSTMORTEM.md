# Engineering Post-Mortem Analysis (`POSTMORTEM.md`)

This document records every significant defect discovered during the multi-agent production of **CivicShield AI Preliminary Report**, analyzing **(1) what failed**, **(2) technical root cause**, **(3) why automated checks initially missed it**, **(4) the permanent architectural fix**, and **(5) the preventive guardrail added to our Detector/Fixer workflow**.

---

## Incident 1: Global Horizontal Shift of All `tcolorbox` & `\tcbox` Frames in LuaLaTeX RTL
- **Symptom:** Every `tcolorbox` (`insightbox`, `riskbox`, `contractbox`, cover metadata box, chapter banners, `ltrcode`) and inline `\tcbox` (section number badges, footer `\CSPagePill`) rendered with its background frame shifted one full width to the right—often off the page—while text remained centered or became invisible (white text on white background).
- **Root Cause:**
  1. Under `babel` (`bidi=basic`) in LuaLaTeX, `pgfpicture` boxes created inside a `hebrew` (`TRT`) paragraph inherit `TRT` box direction, placing the `\pdfliteral` origin at the right edge so the drawn box extends rightward off-page.
  2. Our initial fix (`before={\par\noindent\begingroup\pardir TLT\textdir TLT}`) failed on callout boxes for two subtle reasons: (a) `before skip=12pt` / `after skip=12pt` in `tcolorbox` silently **overwrote** `before=` / `after=`, and (b) `tcolorbox` typesets `attach boxed title` pills *before* executing `before=`, while `babel`'s node attribute was still `hebrew`.
- **Why It Went Undetected Initially:** `lualatex` exited with `0` errors and `0` warnings; `verify_report.py` only parsed `.log` files and `.tex` syntax rather than rendering visual PNGs.
- **Permanent Fix (`civicshield.cls`):**
  - Wrapped `insightbox`, `riskbox`, `contractbox`, and `ltrcode` via `etoolbox` (`\BeforeBeginEnvironment{...}{\begin{otherlanguage}{english}}` / `\AfterEndEnvironment`), restored Hebrew inside bodies via `before upper={\selectlanguage{hebrew}}`, and wrapped floating pill titles in `\foreignlanguage{hebrew}{#1}`.
  - Wrapped inline `\tcbox` badges (`\CSPagePill` and `\titleformat{\section}`) in `\foreignlanguage{english}{...}` and switched `\pageref{LastPage}` to `\pageref*{LastPage}` so link coloring did not turn white pill text navy.
- **Preventive Guardrail:** Added mandatory `pdftoppm -png` page rendering and visual inspection of every box type to `skills/qa-detector/SKILL.md`.

---

## Incident 2: Cover Page Headline & Footer Aligned Left Instead of Right in RTL
- **Symptom:** Cover page eyebrow, main title, subtitle, and bottom copyright footer aligned flush-left (towards the shield emblem) instead of flush-right.
- **Root Cause:** Standard LaTeX `\raggedleft` and `\begin{flushright}` insert infinite stretchable glue at `\leftskip`. In LuaTeX `\pardir TRT` (right-to-left paragraphs), `\leftskip` is the **starting (right)** edge—so `\raggedleft` pushed Hebrew text to the **left**, whereas `\raggedright` puts glue on the left edge and flushes text cleanly to the **right**.
- **Why It Went Undetected Initially:** Instinctive LTR LaTeX conventions (`\raggedleft` = "right-aligned") behave inversely inside `TRT` minipages; only direct visual inspection of rendered page 1 caught it.
- **Permanent Fix (`civicshield.cls`):** Switched `\raggedleft` and `\begin{flushright}` on page 1 to `\raggedright` (with `\vspace*{4mm}` clearance above the bottom gold rule), visually verified via `assets/report_p01_cover.png`.

---

## Incident 3: Figure 3.1 TikZ Text Clipping Under Side Pillars & Awkward Hyphenation
- **Symptom:** Text in Layers 1–3 of Figure 3.1 (`ch03_architecture.tex`) extended horizontally underneath the `Zero-Trust Security` and `Observability & Ops` vertical pillars, and `Observability` broke awkwardly as `Observ-ability`.
- **Root Cause:** `layer/.style` set `minimum width=10.2cm` without constraining `text width`, allowing wide single-line descriptions to expand beyond `10.2cm` into the adjacent pillar coordinates (`x = ±6.35cm`).
- **Why It Went Undetected Initially:** TikZ node overlaps produce no LaTeX warnings or `Overfull \hbox` messages.
- **Permanent Fix (`chapters/ch03_architecture.tex`):** Set explicit `text width=11.0cm`, `minimum width=11.4cm`, `\scriptsize` subtitles, vertical spacing `1.72cm`, moved pillars to `x = ±7.35cm`, added `\hyphenpenalty=10000\exhyphenpenalty=10000`, and wrapped the diagram in `\resizebox{\textwidth}{!}{...}`.

---

## Incident 4: Table Header Baseline Drop in `tabularx`/`longtable` & `74.45pt` Code Path Overflow
- **Symptom:** (a) Dark-navy table headers in `p{}` and `X` columns dropped onto a lower baseline than `l` columns; (b) `scripts/generate_figures.py` on Ch. 4 §4.6 overflowed `74.45pt` past the left margin; (c) Table 3.2 split `Through-put` and `Availabil-ity`.
- **Root Cause:** (a) `\color{white}` at the start of a vertical-mode parbox inserts a color whatsit before entering horizontal mode; (b) `\texttt` paths without break hints cannot wrap; (c) narrow `p{2.8cm}` column forced mid-word hyphenation.
- **Why It Went Undetected Initially:** Minor visual typography flaws only stood out once full pages were rendered and `Overfull \hbox` logs were audited.
- **Permanent Fix:** Defined `\newcommand{\thead}[1]{\leavevmode\color{white}\textbf{#1}}` across all tables; inserted `\allowbreak` in `\code{scripts/\allowbreak generate\_figures.py}`; widened Table 3.2 col 2 to `p{3.4cm}` with hyphenation disabled. Max remaining `Overfull \hbox` across all 43 pages dropped from `74.45pt` to `2.57pt`.

---

## Incident 5: MiKTeX Non-Interactive Hang on `biblatex` (`logreq.sty` Missing)
- **Symptom:** Switching from `plain` BibTeX to `biblatex` caused `lualatex` to freeze indefinitely during preamble loading.
- **Root Cause:** `biblatex.sty` was installed locally in MiKTeX, but its transitive dependency `logreq.sty` (and `biblatex-apa`) was not; MiKTeX's package-install prompt blocked silently in a non-interactive terminal.
- **Why It Went Undetected Initially:** Checking only `biblatex.sty` and `biber.exe` did not enumerate transitive `.sty` dependencies.
- **Permanent Fix:** Implemented a zero-dependency native LuaLaTeX APA 7th citation & LTR hanging-indent bibliography engine (`apabibliography` using a canonical `list` with `\leftmargin=0.5in`, `\itemindent=-0.5in`, `otherlanguage{english}`, clickable `\hyperlink`/`\hypertarget` citations, and `chapters/references_apa7.tex` synced 1:1 with `references.bib`). Compilation completed in ~20 seconds with zero external package risk.

---

## Incident 6: Windows LuaTeX Fatal Font Subset Error on Hebrew Italics (`arialni.ttf`)
- **Symptom:** Adding `\textit{עדאלה}` in Chapter 2 caused a fatal LuaTeX error: `(file C:/Windows/Fonts/arialni.ttf) (type 2): there are no glyphs in the subset`.
- **Root Cause:** On Windows fallback font configurations (`Arial`), italic Hebrew resolves to Arial Narrow Italic, which lacks Hebrew glyph outlines.
- **Permanent Fix:** Replaced `\textit{עדאלה}` with `\textbf{עדאלה}` (consistent with existing Hebrew emphasis conventions) and documented the rule in `skills/theory-legal-researcher/SKILL.md` and `skills/qa-fixer/SKILL.md`.

---

## Incident 7: `build.ps1` `Get-FileHash` & `verify_report.py` Hardcoded Machine Path
- **Symptom:** `build.ps1` failed at its final SHA-256 verification step when `Get-FileHash` was unavailable in the shell module path, and `verify_report.py` contained an author-specific local OneDrive path.
- **Permanent Fix:** Replaced `Get-FileHash` in `build.ps1` with built-in `.NET` `[System.Security.Cryptography.SHA256]::Create()`, and refactored `verify_report.py` to resolve all paths dynamically from `Path(__file__).resolve().parent.parent`.
