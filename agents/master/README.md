# CivicShield AI — Preliminary Report (`CivicShield_AI_Preliminary_Report.pdf`)

**Course:** Applied AI & Vibe Coding (University of Haifa, Dr. Yoram Segal)  
**Deliverable:** Government-Tender Grade Preliminary Report (LuaLaTeX Book, 37–45 pages, target 40 pages)

## Project Overview
**CivicShield AI** is a sovereign, multi-agent national cognitive-resilience platform designed to detect coordinated inauthentic behavior (CIB) and foreign information manipulation and interference (FIMI) while strictly enforcing Israeli constitutional safeguards (*Behavior Not Speech*, *Human-in-the-Loop*, *Privacy by Design*, and anti-censorship accountability).

## Multi-Agent Architecture & Ownership
- **`master`**: Project decomposition (`PLAN.md`, `TODO.md`), shared board governance, and final LuaLaTeX assembly (`main.tex` -> `CivicShield_AI_Preliminary_Report.pdf`).
- **`theory`**: Chapter 1 (`chapters/ch01_vision.tex`), Chapter 2 (`chapters/ch02_theory_law.tex`), and `references.bib` (Political Communication, Political Science, Israeli & EU Constitutional Law).
- **`architect`**: Original `civicshield.cls` (custom state-engineering palette, chapter headers, callout boxes, LuaLaTeX BiDi), `main.tex` front matter, and Chapter 3 (`chapters/ch03_architecture.tex` with pure TikZ diagrams and FR/NFR matrices).
- **`simulator`**: `scripts/generate_figures.py` (SIRI ODE, Hegselmann-Krause opinions, Bayesian fusion, M/M/c queueing, 5-year ROI) and Chapter 4 (`chapters/ch04_simulations.tex`).
- **`redteam`**: Chapter 5 (`chapters/ch05_safeguards_audit.tex`), Dual RedTeam -> ReAct Audit (constitutionality, anti-censorship, numerical consistency, `verify_report.py`, LuaLaTeX BiDi & visual QA).

## Build & Run Instructions
1. **Generate Simulation Figures:**
   ```powershell
   py scripts/generate_figures.py
   ```
2. **Compile PDF (LuaLaTeX + BibTeX):**
   ```powershell
   lualatex -interaction=nonstopmode main.tex
   bibtex main
   lualatex -interaction=nonstopmode main.tex
   lualatex -interaction=nonstopmode main.tex
   Copy-Item main.pdf CivicShield_AI_Preliminary_Report.pdf -Force
   ```
3. **Run Automated QA Verification:**
   ```powershell
   py scripts/verify_report.py
   ```

## Current Milestone Status
- [x] Phase 1: Parallel drafting by `theory`, `architect`, `simulator`, `redteam`
- [x] Phase 2: Initial LuaLaTeX assembly (`CivicShield_AI_Preliminary_Report.pdf` generated)
- [x] Phase 3: RedTeam -> ReAct Dual Audit & BiDi QA (`verify_report.py`: 0 LaTeX errors, 0 undefined refs/cites)
- [x] Phase 4: Page layout & Glossary fixes (no pages 8-9 split, no orphaned headings via `needspace`/`\raggedbottom`, intact callout boxes)
- [x] Phase 5: Final build via `build.ps1` & root sync (`CivicShield_AI_Preliminary_Report.pdf`, 39 PDF pages / 38 numbered pages, 935,647 bytes, 0 LaTeX errors)
