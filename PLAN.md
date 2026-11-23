# CivicShield AI — Preliminary Report Master Plan (`PLAN.md`)

**Target Deliverable:** `CivicShield_AI_Preliminary_Report.pdf`
**Format:** Professional LuaLaTeX Book (Hebrew RTL + English LTR BiDi, original `civicshield.cls` styling, TikZ diagrams only, Python-generated vector figures)
**Target Length:** 40 pages (acceptable range: 37–45 pages)  
**Final Verified Status:** ✅ **COMPLETED** — `CivicShield_AI_Preliminary_Report.pdf` (**39 PDF pages / 38 numbered pages**, continuous Arabic numbering, `935,647` bytes, `0` LaTeX errors, `0` undefined refs/cites)

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
3. **Phase 3 (Final Assembly, Layout Polish & Documentation — ✅ Completed):**
   - Completed `redteam` Dual RedTeam -> ReAct Audit & BiDi QA fixes (`verify_report.py`: 0 LaTeX errors, 0 BiDi/math errors, 0 undefined refs/cites).
   - Completed `architect` page layout & Glossary fixes: unified Glossary onto page 8 (eliminated pages 8–9 split), eliminated orphaned section headings (`2.6`, `3.5`, `4.2`) via `needspace` + `\raggedbottom` + widow/club penalties, kept callout boxes intact, and added clean `\clearpage` before section 4.6.
   - Rebuilt and synced `CivicShield_AI_Preliminary_Report.pdf` via `agents/master/build.ps1` (**39 PDF pages / 38 numbered**, `935,647` bytes, SHA-256 verified, **0 LaTeX errors**).
   - Updated `README.md`, `PRD.md`, `PLAN.md`, `TODO.md`, and `agents/master/README.md` to reflect the final verified state.
