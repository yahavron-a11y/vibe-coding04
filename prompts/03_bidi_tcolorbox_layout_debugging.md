# Prompt 03: Visual Detector/Fixer Debugging Loop (BiDi, `tcolorbox`, Cover & Diagrams)

## Engineering Context
- **Stage:** Phase 2 Iterative Visual QA (`qa-detector` + `qa-fixer` + `redteam`)
- **Trigger:** Human visual review revealed shifted `tcolorbox` frames, missing/misaligned cover headlines, clipped TikZ labels in Figure 3.1, and a `74.45pt` Overfull `\hbox` in Chapter 4.
- **Root-Cause Verification Method:** Rendering compiled PDF pages to PNG via `pdftoppm -png` after every single edit and inspecting them directly rather than trusting 0-error `.log` output alone.

## Collaborative Dispatch Prompt Used
```text
Visual inspection of the rendered PDF revealed 5 concrete bugs:
(1) EVERY tcolorbox and tcbox (cover metadata box, insightbox, riskbox, contractbox, chapter banners, section number badges, footer CSPagePill, ltrcode) has its drawn frame shifted one full width to the right in LuaLaTeX + babel(bidi=basic) — note before skip/after skip overwrote before/after, and floating boxed title pills inherit hebrew node direction;
(2) Figure 3.1 (ch03_architecture.tex) layer text clips underneath the left/right vertical pillars and Observability hyphenates awkwardly;
(3) Table 3.2 (NFR) column 2 splits Through-put and Availabil-ity mid-word;
(4) tabularx/longtable header cells with \color{white}\textbf{...} in p/X columns drop to a second line because \color enters vertical mode without \leavevmode;
(5) ch04 line 162 has a 74.45pt Overfull hbox on \code{scripts/generate_figures.py}.

Architect, RedTeam, Theory, and Simulator: diagnose exact root causes, cross-verify fixes with each other until unanimous agreement, and confirm zero visual regressions on rendered PNGs.
```

## Follow-Up Prompt (Cover Page Right-Alignment in RTL)
```text
On the first page, the headline text is left-aligned; edit it so that it is right-aligned (accounting for LuaTeX \pardir TRT where \raggedright flushes right and \raggedleft flushes left), clear of the left-side shield emblem, with zero clipping, and align the bottom footer line to the same right margin.
```

## Key Outcomes
- Eliminated 100% of `tcolorbox` / `\tcbox` / floating title-pill horizontal shifts across all pages.
- Fixed Figure 3.1 clipping, Table 3.2 hyphenation, all dark-navy table header baselines (`\thead`), and dropped max `Overfull \hbox` from `74.45pt` to `2.57pt`.
- Logged all root causes and detection gaps in `POSTMORTEM.md`.
