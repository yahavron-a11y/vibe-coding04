---
name: qa-fixer
description: Dedicated Error Fixer QA agent that receives structured defect reports from qa-detector, implements minimal root-cause fixes in LaTeX/TikZ/Python, rebuilds the PDF, and submits visual proof back to qa-detector.
---

# Skill: Quality Control — Error Fixer (`qa-fixer`)

## Mandate
The **Fixer** consumes the `qa-detector` defect list, fixes root causes systematically (never superficial hacks), rebuilds cleanly via `build.ps1`, and returns updated rendered pages to `qa-detector` and `redteam` for verification.

## Standard Remediation Patterns
1. **LuaLaTeX RTL `tcolorbox` / `\tcbox` Shift:** Wrap block boxes via `\BeforeBeginEnvironment` / `\AfterEndEnvironment` in `otherlanguage{english}` with `before upper={\selectlanguage{hebrew}}` and `\foreignlanguage{hebrew}{#1}` titles; remove `before skip`/`after skip` overrides.
2. **RTL Alignment Inversion:** In `\pardir TRT`, use `\raggedright` for flush-right alignment (never `\raggedleft` or `flushright`).
3. **Table Header Baseline Drop:** Replace `\color{white}\textbf{...}` in `p{}`/`X` columns with `\thead{...}` (`\leavevmode\color{white}\textbf{#1}`).
4. **Overfull `\hbox` on Paths/Code:** Insert `\allowbreak` after `/` or configure `\UrlBreaks` for clean wrapping.
5. **Windows LuaTeX Hebrew Italic Font Crash:** Replace `\textit{<Hebrew>}` with `\textbf{<Hebrew>}` when system fallback italic fonts lack Hebrew glyphs.
6. **Post-Mortem Logging:** After every user-discovered or multi-pass bug is closed, record root cause, detection gap, and preventive guardrail in `POSTMORTEM.md`.
