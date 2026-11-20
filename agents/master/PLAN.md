# CivicShield AI — Preliminary Report Master Plan (`PLAN.md`)

**Target Deliverable:** `CivicShield_AI_Preliminary_Report.pdf`
**Format:** Professional LuaLaTeX Book (Hebrew RTL + English LTR BiDi, original `civicshield.cls` styling, TikZ diagrams only, Python-generated vector figures)
**Target Length:** 40 pages (acceptable range: 37–45 pages)

## Chapter Allocation & Page Targets

| Section | Owner | Target Pages | Key Deliverables |
| :--- | :--- | :---: | :--- |
| **Front Matter** (Cover, Executive Summary, TOC, LOF/LOT) | `architect` / `master` | 5 | `main.tex`, `civicshield.cls`, executive summary |
| **Ch. 1: National Threat Landscape & Strategic Vision** | `theory` | 6 | `chapters/ch01_vision.tex` |
| **Ch. 2: Political Science, Communication & Constitutional Law** | `theory` | 8 | `chapters/ch02_theory_law.tex`, `references.bib` |
| **Ch. 3: 5-Layer Architecture, Multi-Agent Hub & FR/NFRs** | `architect` | 9 | `chapters/ch03_architecture.tex`, TikZ diagrams |
| **Ch. 4: Mathematical Modeling, Simulations & 5-Year ROI** | `simulator` | 8 | `chapters/ch04_simulations.tex`, `scripts/generate_figures.py`, generated figures |
| **Ch. 5: Constitutional Safeguards, Anti-Censorship & QA Audit** | `redteam` | 4 | `chapters/ch05_safeguards_audit.tex`, BiDi & RedTeam QA report |
| **Total** | **All** | **40** | `CivicShield_AI_Preliminary_Report.pdf` |

## Dependencies & Execution Phases
1. **Phase 1 (Parallel Drafting):** `architect` builds `civicshield.cls`, `main.tex`, and Ch. 3 (with TikZ); `theory` drafts Ch. 1–2 and `references.bib`; `simulator` writes/runs `scripts/generate_figures.py` and drafts Ch. 4; `redteam` drafts Ch. 5 and prepares the Constitutional/Anti-Censorship/BiDi QA checklist.
2. **Phase 2 (RedTeam -> ReAct Dual Audit Loop):**
   - **Content & Constitutionality:** RFP compliance, constitutional safeguards, anti-censorship mechanisms, cross-chapter numerical consistency, and academic quality.
   - **Technical & Visual QA:** Run `py scripts/verify_report.py`, check `lualatex` compilation, verify page count (37–45, target 40), detect BiDi errors and Overfull hbox overflows, and render PDF pages for page-by-page visual inspection.
   - **Rejection Loop:** If defects are found, `redteam` reports to `master`, who routes a ReAct Revision task to the responsible peer until full approval.
3. **Phase 3 (Final Assembly & Documentation):**
   - Compile `main.tex` with `lualatex` (including bibliography and TOC) to produce `CivicShield_AI_Preliminary_Report.pdf`.
   - Update `README.md` at each milestone and before any `git push` (project overview, component roles, build & run instructions).
   - Deliver final summary report: final page count, figures/diagrams status, `verify_report.py` results, and RedTeam Loop rounds log.
