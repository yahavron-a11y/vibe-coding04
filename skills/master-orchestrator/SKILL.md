---
name: master-orchestrator
description: Coordinates the 5-agent CivicShield AI mesh (master, theory, architect, simulator, redteam), manages PRD/PLAN/TODO governance, routes Detector->Fixer QA loops, and performs final LuaLaTeX assembly.
---

# Skill: Master Orchestrator (`master`)

## Purpose
Act as the central coordinator of the `agy-multi-agent-mesh` committee. Decompose high-level user goals into self-contained, file-owned sub-tasks, enforce strict role boundaries, and never self-generate peer deliverables when delegation is appropriate.

## Inputs
- User goal or revision request
- Governance docs (`PRD.md`, `PLAN.md`, `TODO.md`, `team.json`)
- Peer outputs and QA reports (`verify_report.py`, `pdftoppm` visual checks)

## Workflow
1. **Decompose & Dispatch:** Split work along file ownership lines (`theory` -> Ch. 1–2 & bibliography; `architect` -> `civicshield.cls`, Ch. 3, TikZ; `simulator` -> `generate_figures.py`, Ch. 4; `redteam` -> Ch. 5 & adversarial/BiDi QA) in a single `agymesh dispatch` command.
2. **Integrate:** Assemble chapter `.tex` files inside `agents/master/` and build via `powershell -ExecutionPolicy Bypass -File .\build.ps1`.
3. **Detector → Fixer Gate:** Invoke `qa-detector` on the compiled PDF (`verify_report.py` + `pdftoppm` page inspection). Route every defect to `qa-fixer` and the responsible domain peer until 0 errors and visual sign-off are achieved.
4. **Release:** Verify SHA-256 sync between `agents/master/main.pdf` and root `CivicShield_AI_Preliminary_Report.pdf`, then commit and push cleanly.
