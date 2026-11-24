# Prompt 02: Parallel Chapter Drafting, Custom `.cls` & Python Simulations

## Engineering Context
- **Stage:** Phase 1 Parallel Production across `agy-multi-agent-mesh`
- **Command Pattern:** Single foreground `agymesh dispatch --name master --to <peer>="<sub-task>"`
- **Outputs:** `civicshield.cls`, `main.tex`, `chapters/ch01..ch05.tex`, `scripts/generate_figures.py`, `figures/fig4_1..fig4_5.{pdf,png}`, `references.bib`

## Prompts Dispatched per Agent

### To `theory` (Chapters 1–2 & Bibliography)
```text
Draft chapters/ch01_vision.tex (National Threat Landscape, FIMI/CIB taxonomy, Strategic Vision, 3-Phase Roadmap, KPIs) and chapters/ch02_theory_law.tex (Political Communication, Defensive Democracy, Inoculation/Prebunking, Israeli Constitutional Law & EU DSA/AI Act, Democratic Governance) in publication-grade Hebrew with English terms wrapped in \textenglish{...} or \en{...}. Provide complete academic and legal sources in references.bib.
```

### To `architect` (Template & Chapter 3)
```text
Design an original executive LuaLaTeX book class (civicshield.cls) using a sovereign navy/gold/teal/crimson color palette, custom TikZ cover page with a vector shield + neural-grid emblem, custom chapter/section headers, callout boxes (insightbox, riskbox, contractbox, ltrcode), and Arabic page numbering. Draft chapters/ch03_architecture.tex covering the 5-Layer Architecture, Multi-Agent Hub-and-Spoke specification, Agent-to-Hub JSON SLA contract, FR-01..FR-10 & NFR-01..NFR-10 matrices, and 3 pure-TikZ diagrams (no external images).
```

### To `simulator` (Python Simulation Core & Chapter 4)
```text
Write a deterministic, production-grade Python 3.11+ script (scripts/generate_figures.py) with strict type hints, frozen dataclasses, and numerical safeguards to simulate and export 5 vector PDF + 300-DPI PNG figures: (1) RK4 SIRI ODE disinfection/prebunking dynamics, (2) Hegselmann-Krause opinion dynamics, (3) log-odds Bayesian multi-modal fusion & ROC, (4) log-space Erlang-C M/M/c SOC queueing, and (5) 5-year TCO/NPV/ROI financial model. Draft chapters/ch04_simulations.tex integrating all equations, tables, figures, and a hardened Python reference listing.
```

### To `redteam` (Chapter 5 & Automated QA Script)
```text
Draft chapters/ch05_safeguards_audit.tex auditing Constitutional-by-Design invariants, anti-censorship guarantees, false-positive traps, 4-tier democratic oversight, and quarterly Red-Team methodology. Write scripts/verify_report.py to validate PDF page count, 0 LaTeX compilation errors, 0 undefined references/citations, and BiDi math hygiene.
```
