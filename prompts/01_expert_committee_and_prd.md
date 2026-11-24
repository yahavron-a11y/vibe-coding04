# Prompt 01: Expert Committee Formation & PRD Generation

## Engineering Context
- **Stage:** Project Initialization & Governance Blueprint
- **Target Agent:** `master` (coordinating the 5-agent Expert Committee via `agy-multi-agent-mesh`)
- **Outputs:** `PRD.md`, `PLAN.md`, `TODO.md`, `team.json`

## Prompt Used
```text
Act as an interdisciplinary Expert Committee (Political Communication & Constitutional Law Professor, Sovereign Cloud Systems Architect, Applied Mathematician/Quantitative Modeler, and Adversarial Red-Team Auditor) tasked with drafting the Product Requirements Document (PRD.md), Master Execution Plan (PLAN.md), Shared TODO Board (TODO.md), and agy-multi-agent-mesh configuration (team.json) for a ~40-page Hebrew government-tender Preparatory Report:

Project: "CivicShield AI — National Cognitive Resilience & Multi-Agent Information Integrity Platform"

Mandatory Constraints:
1. Treat the report as a binding government-tender engineering & legal contract (Hebrew RTL with isolated English terminology).
2. Enforce "Behavior Not Speech" (Zero Auto-Censorship), Human-in-the-Loop (HITL), and Israeli/EU legal compliance (Basic Law: Human Dignity and Liberty, Kol Ha'am, Adalah, Privacy Law Amendment 13, EU DSA & AI Act).
3. Define strict file ownership across 5 mesh agents (master, theory, architect, simulator, redteam) to prevent merge conflicts and context pollution.
4. Require LuaLaTeX compilation with a custom .cls document class, pure-TikZ diagrams (zero internet images), 5 deterministic Python mathematical simulations, and an automated Red-Team / Detector-Fixer QA loop.
```

## Outcome & Lessons Learned
- Establishing explicit file ownership in `team.json` eliminated cross-agent overwrite conflicts during parallel dispatches.
- Separating constitutional constraints into `PRD.md` Section 2 allowed `redteam` to audit every subsequent chapter against objective Pass/Fail invariants.
