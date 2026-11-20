# CivicShield AI — Shared TODO Board (`TODO.md`)

- [x] **[architect]** Create original `civicshield.cls` (custom state-engineering palette, chapter headers, insight/risk/contract callout boxes, custom headers/footers, LuaLaTeX BiDi Hebrew/English support) and modular `main.tex`.
- [x] **[architect]** Write Chapter 3 (`chapters/ch03_architecture.tex`, ~9 pages): 5-Layer Architecture, Multi-Agent Hub Specification, FR/NFR tables, and pure-TikZ architectural diagrams (no external images).
- [x] **[theory]** Write Chapter 1 (`chapters/ch01_vision.tex`, ~6 pages) & Chapter 2 (`chapters/ch02_theory_law.tex`, ~8 pages) in Hebrew with English terms: Threat Landscape, Political Communication, Political Science, Constitutional Law, and `references.bib`.
- [x] **[simulator]** Write and execute `scripts/generate_figures.py` (`py scripts/generate_figures.py`) to generate vector/high-res figures for SIRI ODE, Hegselmann-Krause opinions, Bayesian fusion, M/M/c queueing, and 5-year ROI.
- [x] **[simulator]** Write Chapter 4 (`chapters/ch04_simulations.tex`, ~8 pages) in Hebrew with equations, tables, and embedded generated figures.
- [x] **[redteam]** Write Chapter 5 (`chapters/ch05_safeguards_audit.tex`, ~4 pages): Constitutional Safeguards Audit, Anti-Censorship Review, and Implementation Governance.
- [x] **[redteam]** Conduct Dual RedTeam -> ReAct Audit: (a) Content & Constitutionality (RFP compliance, safeguards, anti-censorship, cross-chapter numerical consistency, academic quality); (b) Technical & Visual QA (`py scripts/verify_report.py`, `lualatex` check, 37–45 page count, BiDi errors, Overfull hbox, page-by-page PDF visual inspection).
- [x] **[master]** Route any RedTeam Rejection Loop defects as ReAct Revision tasks to responsible peers until full approval.
- [x] **[master]** Final `lualatex` compilation (with bibliography & TOC) of `CivicShield_AI_Preliminary_Report.pdf`, update `README.md` at milestones, and deliver final summary report.
