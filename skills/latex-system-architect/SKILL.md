---
name: latex-system-architect
description: Designs the 5-layer Multi-Agent Hub architecture, FR/NFR matrices, Sovereign DRP topology, custom civicshield.cls LuaLaTeX BiDi template, and code-only TikZ diagrams.
---

# Skill: System Architecture & LuaLaTeX/TikZ Design (`architect`)

## Role & Ownership
- **Owned Files:** `civicshield.cls`, `main.tex`, `chapters/ch03_architecture.tex`
- **Domain:** 5-layer Sovereign Cloud architecture, Multi-Agent Hub-and-Spoke specification, FR/NFR matrices, DRP/Air-Gap failover, and bespoke LuaLaTeX visual identity.

## Engineering & Typography Rules
1. **Code-Only Illustrations:** Zero external or internet images. All diagrams (cover shield emblem, 5-layer architecture, Hub-and-Spoke topology, P95 latency pipeline) must be pure TikZ code.
2. **LuaLaTeX + `babel(bidi=basic)` Safety:**
   - Wrap all `tcolorbox` environments (`insightbox`, `riskbox`, `contractbox`, `ltrcode`, cover metadata box) in `\BeforeBeginEnvironment{...}{\begin{otherlanguage}{english}}` so `pgfpicture` frames and floating `boxed title` pills render in deterministic `TLT` coordinates without shifting right.
   - Restore Hebrew RTL inside box bodies (`before upper={\selectlanguage{hebrew}}`) and wrap floating titles in `\foreignlanguage{hebrew}{#1}`.
   - Wrap inline `\tcbox` badges (`\CSPagePill`, section badges) in `\foreignlanguage{english}{...}`.
   - Remember that in LuaTeX `\pardir TRT`, `\raggedright` flushes text to the **right** margin while `\raggedleft` flushes text to the **left**.
3. **Table & Diagram Hygiene:** Use `\thead{...}` (`\leavevmode\color{white}\textbf{#1}`) for dark-navy header rows to prevent parbox baseline drops; bound TikZ figures with `\resizebox{\textwidth}{!}` and `\hyphenpenalty=10000`.
