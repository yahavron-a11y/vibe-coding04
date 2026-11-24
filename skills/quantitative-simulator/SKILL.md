---
name: quantitative-simulator
description: Implements deterministic, production-grade Python mathematical simulations (SIRI ODE, Hegselmann-Krause, Bayesian Fusion, M/M/c Erlang-C, 5-Year ROI) and authors Chapter 4 with sensitivity analysis.
---

# Skill: Quantitative Modeling & Python Simulation (`simulator`)

## Role & Ownership
- **Owned Files:** `scripts/generate_figures.py`, `figures/fig4_1..fig4_5.{pdf,png}`, `chapters/ch04_simulations.tex`
- **Domain:** Applied mathematics, epidemiological modeling (RK4 SIRI ODEs), bounded-confidence opinion dynamics (Hegselmann-Krause), log-odds Bayesian sensor fusion, log-space Erlang-C queueing (`M/M/c`), and 5-year TCO/NPV/ROI financial modeling.

## Quality Standards
1. **Numerical Stability & Determinism:** Use strict Python 3.11+ type hints, frozen dataclasses, unit-simplex conservation invariants, log-odds clamping, and `lgamma` log-sum-exp Erlang-C computation.
2. **Dual Vector + Raster Output:** Export every plot as both publication-grade vector `.pdf` (for LuaLaTeX) and 300-DPI `.png` (for `README.md`) with clean non-overlapping legends and annotations.
3. **Cross-Document Numeric Consistency:** Every KPI in prose, tables, captions, and sensitivity stress-tests (`R_eff=0.81`, Peak `0.8%`, `AUC=0.964`, `rho=51.9%`, `NPV=+42.6M ILS`, `ROI=204.6%`) must match the Python simulation outputs exactly.
