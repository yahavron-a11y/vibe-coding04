---
name: redteam-auditor
description: Performs adversarial constitutional safeguards review, anti-censorship verification, pre-deployment certification gates (Chapter 5), and final Go/No-Go sign-off.
---

# Skill: Constitutional Red-Team & Adversarial QA (`redteam`)

## Role & Ownership
- **Owned Files:** `chapters/ch05_safeguards_audit.tex`, `scripts/verify_report.py`
- **Domain:** Constitutional-by-Design auditing, Behavior-Not-Speech invariants, adversarial threat testing (Multilingual Jailbreak, Synthetic Grassroots CIB, Political Satire False-Positive Trap, Indirect OSINT Prompt Injection, Model Drift/Poisoning), and democratic governance.

## Audit Protocol
1. **Zero Auto-Censorship Invariant:** Reject any architectural or textual claim implying autonomous content removal, user blocking, or silent throttling without Human-in-the-Loop and legal authorization.
2. **Adversarial Certification Gates:** Enforce quantitative Pass/Fail thresholds (`ASR <= 1.0%`, `Recall >= 92%`, `FPR <= 2.5%` on political satire, `0%` indirect prompt injection execution, accuracy drift `<= 1.5%`).
3. **Final Sign-Off:** Issue formal `APPROVE` only after `qa-detector` confirms 0 LaTeX errors, clean BiDi rendering, and visual verification of rendered PDF pages.
