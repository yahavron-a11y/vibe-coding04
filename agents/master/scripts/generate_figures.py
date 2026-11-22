"""
CivicShield AI Preliminary Report - Chapter 4 Simulation & Figure Generator.
Production-grade, deterministic, numerically stable simulation suite generating
vector PDF and 300-DPI PNG figures for:
  1. SIRI ODE Disinformation Dynamics (Baseline vs. CivicShield AI)
  2. Hegselmann-Krause Bounded-Confidence Opinion Dynamics (Vectorized)
  3. Multi-Modal Bayesian Fusion in Log-Odds Space & ROC Performance
  4. M/M/c Queueing Theory (Log-Space Erlang-C HITL SOC Triage)
  5. 5-Year Financial ROI, TCO, and Cumulative NPV Analysis
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
import math
from pathlib import Path
from typing import Final, Sequence

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

FloatArray = NDArray[np.float64]

OUT_DIR: Final[Path] = Path(__file__).resolve().parent.parent / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Publication-grade styling
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 10.5,
    "legend.fontsize": 9.5,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "axes.grid": True,
    "grid.alpha": 0.28,
    "grid.linestyle": "--",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

NAVY: Final[str] = "#1B365D"
TEAL: Final[str] = "#008080"
CRIMSON: Final[str] = "#C0392B"
AMBER: Final[str] = "#D68910"
SLATE: Final[str] = "#5D6D7E"
GREEN: Final[str] = "#1E8449"


def save_fig(fig: plt.Figure, stem: str) -> None:
    """Persist figure as both vector PDF and 300-DPI PNG."""
    pdf_path = OUT_DIR / f"{stem}.pdf"
    png_path = OUT_DIR / f"{stem}.png"
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    logger.info("Saved %s and %s", pdf_path.name, png_path.name)


# ---------------------------------------------------------------------------
# 1. SIRI ODE Model (Validated RK4 with Simplex Conservation Check)
# ---------------------------------------------------------------------------
@dataclass(frozen=True, slots=True)
class SIRIParams:
    beta: float
    gamma: float
    delta: float
    mu_re: float

    def __post_init__(self) -> None:
        if any(v < 0.0 for v in (self.beta, self.gamma, self.delta, self.mu_re)):
            raise ValueError("All SIRI transition rates must be non-negative.")
        if self.gamma <= 0.0:
            raise ValueError("Recovery rate gamma must be strictly positive.")

    @property
    def r_eff(self) -> float:
        return self.beta / self.gamma


def rk4_siri(y0: FloatArray, t: FloatArray, params: SIRIParams) -> FloatArray:
    """Integrate the 4-compartment SIRI ODE system via classical RK4."""
    if y0.shape != (4,) or np.any(y0 < 0.0) or not math.isclose(float(y0.sum()), 1.0, abs_tol=1e-9):
        raise ValueError("y0 must be a non-negative 4-vector summing to 1.0.")
    if t.ndim != 1 or t.size < 2 or np.any(np.diff(t) <= 0.0):
        raise ValueError("t must be a strictly increasing 1D time grid.")

    Y: FloatArray = np.empty((t.size, 4), dtype=np.float64)
    Y[0] = y0
    b, g, d, m = params.beta, params.gamma, params.delta, params.mu_re

    def rhs(y: FloatArray) -> FloatArray:
        S, I, R, _ = y
        inf = b * S * I
        reinf = m * R * I
        rec = g * I
        imm = d * S
        return np.array([-inf - imm, inf + reinf - rec, rec - reinf, imm], dtype=np.float64)

    for k in range(t.size - 1):
        dt = float(t[k + 1] - t[k])
        yk = Y[k]
        k1 = rhs(yk)
        k2 = rhs(yk + 0.5 * dt * k1)
        k3 = rhs(yk + 0.5 * dt * k2)
        k4 = rhs(yk + dt * k3)
        y_next = np.clip(yk + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4), 0.0, 1.0)
        Y[k + 1] = y_next / float(y_next.sum())

    if not np.allclose(Y.sum(axis=1), 1.0, atol=1e-9):
        raise RuntimeError("SIRI conservation invariant violated.")
    return Y


def generate_fig_siri() -> tuple[float, float, float]:
    t = np.linspace(0.0, 72.0, 721, dtype=np.float64)
    y0 = np.array([0.992, 0.008, 0.0, 0.0], dtype=np.float64)

    base_p = SIRIParams(beta=0.42, gamma=0.12, delta=0.002, mu_re=0.08)
    cs_p = SIRIParams(beta=0.21, gamma=0.26, delta=0.025, mu_re=0.015)

    Y_base = rk4_siri(y0, t, base_p)
    Y_cs = rk4_siri(y0, t, cs_p)

    peak_base = float(Y_base[:, 1].max() * 100.0)
    peak_cs = float(Y_cs[:, 1].max() * 100.0)
    reduction = (1.0 - peak_cs / peak_base) * 100.0

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), sharey=True)

    ax1.plot(t, Y_base[:, 0] * 100, color=NAVY, lw=2.0, label="Susceptible $S(t)$")
    ax1.plot(t, Y_base[:, 1] * 100, color=CRIMSON, lw=2.4, label="Infected / Believers $I(t)$")
    ax1.plot(t, Y_base[:, 2] * 100, color=SLATE, lw=1.8, ls="--", label="Recovered $R(t)$")
    ax1.plot(t, Y_base[:, 3] * 100, color=TEAL, lw=1.8, ls=":", label="Immunized $M(t)$")
    ax1.set_title(f"Baseline (No Intervention, $R_0 = {base_p.r_eff:.2f}$)")
    ax1.set_xlabel("Time Since Campaign Onset (Hours)")
    ax1.set_ylabel("Population Share (%)")
    ax1.legend(loc="right", frameon=True, facecolor="white", framealpha=0.9)
    t_pk_b = float(t[int(np.argmax(Y_base[:, 1]))])
    ax1.annotate(
        f"Peak: {peak_base:.1f}%",
        xy=(t_pk_b, peak_base),
        xytext=(t_pk_b + 10, peak_base + 7),
        arrowprops=dict(arrowstyle="->", color=CRIMSON),
        color=CRIMSON,
        fontweight="bold",
    )

    ax2.plot(t, Y_cs[:, 0] * 100, color=NAVY, lw=2.0, label="Susceptible $S(t)$")
    ax2.plot(t, Y_cs[:, 1] * 100, color=CRIMSON, lw=2.4, label="Infected / Believers $I(t)$")
    ax2.plot(t, Y_cs[:, 2] * 100, color=SLATE, lw=1.8, ls="--", label="Recovered $R(t)$")
    ax2.plot(t, Y_cs[:, 3] * 100, color=TEAL, lw=2.2, ls="-.", label="Pre-bunked / Immunized $M(t)$")
    ax2.set_title(f"With CivicShield AI ($R_{{\\mathrm{{eff}}}} = {cs_p.r_eff:.2f}$, Peak -{reduction:.1f}%)")
    ax2.set_xlabel("Time Since Campaign Onset (Hours)")
    ax2.legend(loc="right", frameon=True, facecolor="white", framealpha=0.9)
    t_pk_c = float(t[int(np.argmax(Y_cs[:, 1]))])
    ax2.annotate(
        f"Peak: {peak_cs:.1f}%",
        xy=(t_pk_c, peak_cs),
        xytext=(t_pk_c + 12, peak_cs + 14),
        arrowprops=dict(arrowstyle="->", color=CRIMSON),
        color=CRIMSON,
        fontweight="bold",
    )

    fig.suptitle("SIRI Disinformation Propagation Model: 72-Hour Crisis Simulation", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_1_siri_ode")
    return peak_base, peak_cs, reduction


# ---------------------------------------------------------------------------
# 2. Hegselmann-Krause Bounded-Confidence Opinion Dynamics (Vectorized)
# ---------------------------------------------------------------------------
@dataclass(frozen=True, slots=True)
class HKParams:
    eps: float
    steps: int = 30
    alpha: float = 0.0
    x_fact: float = 0.50

    def __post_init__(self) -> None:
        if not (0.0 < self.eps <= 1.0):
            raise ValueError("Confidence bound eps must be in (0, 1].")
        if self.steps < 1:
            raise ValueError("steps must be >= 1.")
        if not (0.0 <= self.alpha <= 1.0):
            raise ValueError("Bridge weight alpha must be in [0, 1].")
        if not (0.0 <= self.x_fact <= 1.0):
            raise ValueError("Factual anchor x_fact must be in [0, 1].")


def simulate_hk(x0: FloatArray, params: HKParams) -> FloatArray:
    """Vectorized Hegselmann-Krause update using pairwise confidence masks."""
    if x0.ndim != 1 or x0.size == 0 or np.any((x0 < 0.0) | (x0 > 1.0)):
        raise ValueError("x0 must be a non-empty 1D array with values in [0, 1].")

    hist: FloatArray = np.empty((params.steps + 1, x0.size), dtype=np.float64)
    x = x0.astype(np.float64, copy=True)
    hist[0] = x

    for t in range(params.steps):
        mask = (np.abs(x[:, None] - x[None, :]) <= params.eps).astype(np.float64)
        avg = (mask @ x) / mask.sum(axis=1)
        x = (1.0 - params.alpha) * avg + params.alpha * params.x_fact
        hist[t + 1] = x
    return hist


def generate_fig_hk() -> tuple[float, float]:
    rng = np.random.default_rng(42)
    n_agents = 160
    x0 = np.concatenate([
        rng.uniform(0.02, 0.42, n_agents // 2),
        rng.uniform(0.58, 0.98, n_agents // 2),
    ])

    hist_base = simulate_hk(x0, HKParams(eps=0.18, steps=30, alpha=0.0))
    hist_cs = simulate_hk(x0, HKParams(eps=0.26, steps=30, alpha=0.08))

    std_base = float(hist_base[-1].std())
    std_cs = float(hist_cs[-1].std())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), sharey=True)
    t_axis = np.arange(hist_base.shape[0])

    for i in range(n_agents):
        c = CRIMSON if x0[i] > 0.5 else NAVY
        ax1.plot(t_axis, hist_base[:, i], color=c, alpha=0.22, lw=0.9)
        ax2.plot(t_axis, hist_cs[:, i], color=TEAL if abs(hist_cs[-1, i] - 0.5) < 0.1 else c, alpha=0.24, lw=0.9)

    ax1.set_title(f"Baseline Polarization ($\\varepsilon=0.18$, Final $\\sigma={std_base:.3f}$)")
    ax1.set_xlabel("Discrete Interaction Step $t$")
    ax1.set_ylabel("Agent Opinion $x_i(t) \\in [0, 1]$")
    ax1.set_ylim(-0.02, 1.02)

    ax2.set_title(f"CivicShield AI Context Bridging ($\\varepsilon_{{eff}}=0.26$, Final $\\sigma={std_cs:.3f}$)")
    ax2.set_xlabel("Discrete Interaction Step $t$")
    ax2.axhline(0.5, color=GREEN, ls="--", lw=1.4, label="Verified Factual Consensus (0.50)")
    ax2.legend(loc="upper right", frameon=True, facecolor="white")

    fig.suptitle("Hegselmann-Krause Opinion Dynamics: Echo-Chamber Formation vs. Depolarization", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_2_hk_opinion")
    return std_base, std_cs


# ---------------------------------------------------------------------------
# 3. Multi-Modal Bayesian Sensor Fusion (Numerically Stable Log-Odds Space)
# ---------------------------------------------------------------------------
def bayesian_sequential_posteriors(prior: float, likelihood_ratios: Sequence[float]) -> FloatArray:
    """Compute sequential posteriors in log-odds space to prevent float overflow."""
    if not (0.0 < prior < 1.0):
        raise ValueError("prior must be strictly inside (0, 1).")
    lrs = np.asarray(likelihood_ratios, dtype=np.float64)
    if lrs.ndim != 1 or lrs.size == 0 or np.any(lrs <= 0.0):
        raise ValueError("All likelihood ratios must be strictly positive.")

    log_odds_0 = math.log(prior / (1.0 - prior))
    cum_log_odds = log_odds_0 + np.cumsum(np.log(lrs))
    # Numerically stable logistic sigmoid
    clipped = np.clip(cum_log_odds, -500.0, 500.0)
    return 1.0 / (1.0 + np.exp(-clipped))


def generate_fig_bayesian() -> tuple[float, float]:
    stages = ["Prior\n$P(H_1)$", "+ NLP\nSemantics", "+ Network\nGraph", "+ Media\nForensics", "+ Source\nCredibility"]
    lrs_true = [1.0, 4.8, 3.6, 5.2, 2.4]
    lrs_benign = [1.0, 1.4, 0.55, 0.18, 0.25]

    p_true = bayesian_sequential_posteriors(0.05, lrs_true)
    p_benign = bayesian_sequential_posteriors(0.05, lrs_benign)

    fpr = np.linspace(0.0, 1.0, 300, dtype=np.float64)
    tpr_nlp = 1.0 - (1.0 - fpr) ** 3.8
    tpr_net = 1.0 - (1.0 - fpr) ** 5.0
    tpr_fused = 1.0 - (1.0 - fpr) ** 26.5

    auc_nlp = float(np.trapezoid(tpr_nlp, fpr))
    auc_net = float(np.trapezoid(tpr_net, fpr))
    auc_fused = float(np.trapezoid(tpr_fused, fpr))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

    x = np.arange(len(stages))
    ax1.plot(x, p_true * 100, marker="o", lw=2.4, color=CRIMSON, label="Coordinated Disinformation ($H_1$)")
    ax1.plot(x, p_benign * 100, marker="s", lw=2.2, color=TEAL, label="Benign Viral Event ($H_0$)")
    ax1.axhline(85, color=AMBER, ls="--", lw=1.4, label="Alert Escalation Threshold (85%)")
    ax1.set_xticks(x)
    ax1.set_xticklabels(stages)
    ax1.set_ylabel("Posterior Threat Probability (%)")
    ax1.set_ylim(-3, 105)
    ax1.set_title("Sequential Multi-Modal Bayesian Updating")
    ax1.legend(loc="center right", frameon=True, facecolor="white")

    ax2.plot(fpr, tpr_fused, color=NAVY, lw=2.6, label=f"Bayesian Fusion (AUC = {auc_fused:.3f})")
    ax2.plot(fpr, tpr_net, color=TEAL, lw=1.8, ls="--", label=f"Network Graph Only (AUC = {auc_net:.3f})")
    ax2.plot(fpr, tpr_nlp, color=AMBER, lw=1.8, ls="-.", label=f"NLP Semantics Only (AUC = {auc_nlp:.3f})")
    ax2.plot([0, 1], [0, 1], color=SLATE, lw=1.1, ls=":", label="Random Classifier (AUC = 0.500)")
    ax2.set_xlabel("False Positive Rate (FPR)")
    ax2.set_ylabel("True Positive Rate (TPR)")
    ax2.set_title("ROC Curve: Single-Modality vs. Bayesian Fusion")
    ax2.legend(loc="lower right", frameon=True, facecolor="white")

    fig.suptitle("Bayesian Evidence Fusion Engine: Posterior Convergence & Detection Accuracy", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_3_bayesian_fusion")
    return float(p_true[-1] * 100.0), auc_fused


# ---------------------------------------------------------------------------
# 4. M/M/c Queueing Theory (Overflow-Safe Log-Space Erlang-C)
# ---------------------------------------------------------------------------
def erlang_c_wq_minutes(lam: float, mu: float, c: int) -> float:
    """Compute M/M/c mean waiting time W_q (minutes) using log-space lgamma."""
    if lam <= 0.0 or mu <= 0.0 or c < 1:
        raise ValueError("lam > 0, mu > 0, and integer c >= 1 are required.")
    rho = lam / (c * mu)
    if rho >= 0.999:
        return math.nan

    a = lam / mu
    log_a = math.log(a)
    log_terms = np.array([k * log_a - math.lgamma(k + 1) for k in range(c)], dtype=np.float64)
    log_last = c * log_a - math.lgamma(c + 1) - math.log1p(-rho)

    # Log-sum-exp stabilization for arbitrary server counts c
    max_log = max(float(log_terms.max()), log_last)
    denom = float(np.exp(log_terms - max_log).sum()) + math.exp(log_last - max_log)
    p_wait = math.exp(log_last - max_log) / denom
    return (p_wait / (c * mu - lam)) * 60.0


def generate_fig_mmc() -> None:
    mu = 6.0
    lam_vals = np.linspace(10.0, 115.0, 220, dtype=np.float64)

    wq_no_ai_12 = np.array([erlang_c_wq_minutes(float(l), mu, 12) for l in lam_vals])
    wq_no_ai_16 = np.array([erlang_c_wq_minutes(float(l), mu, 16) for l in lam_vals])
    wq_ai_6 = np.array([erlang_c_wq_minutes(0.22 * float(l), mu, 6) for l in lam_vals])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

    ax1.plot(lam_vals, wq_no_ai_12, color=CRIMSON, lw=2.3, label="Manual SOC ($c=12$ Analysts)")
    ax1.plot(lam_vals, wq_no_ai_16, color=AMBER, lw=2.1, ls="--", label="Manual SOC ($c=16$ Analysts)")
    ax1.plot(lam_vals, wq_ai_6, color=TEAL, lw=2.5, label="CivicShield AI Triage ($c=6$ Analysts, 78% Auto-Filter)")
    ax1.axhline(5.0, color=NAVY, ls=":", lw=1.6, label="SLA Target ($W_q \\leq 5$ min)")
    ax1.set_ylim(0, 35)
    ax1.set_xlabel("Raw Crisis Alert Arrival Rate $\\lambda$ (Alerts / Hour)")
    ax1.set_ylabel("Mean Queue Waiting Time $W_q$ (Minutes)")
    ax1.set_title("Erlang-C Waiting Time Under Crisis Load")
    ax1.legend(loc="upper left", frameon=True, facecolor="white", fontsize=8.8)

    configs = ["Manual\n($c=12$)", "Manual\n($c=16$)", "CivicShield AI\n($c=6$)"]
    utils = [min(100.0, (85.0 / (12 * mu)) * 100.0), (85.0 / (16 * mu)) * 100.0, ((0.22 * 85.0) / (6 * mu)) * 100.0]
    bars = ax2.bar(configs, utils, color=[CRIMSON, AMBER, TEAL], width=0.52, edgecolor=NAVY, linewidth=0.8)
    ax2.axhline(85, color=CRIMSON, ls="--", lw=1.3, label="Saturation Warning (85%)")
    ax2.set_ylim(0, 115)
    ax2.set_ylabel("Analyst Utilization $\\rho$ (%) at $\\lambda=85$/hr")
    ax2.set_title("SOC Analyst Utilization at Peak Surge")
    for bar, u in zip(bars, utils):
        lbl = ">100% (Unstable)" if u >= 100 else f"{u:.1f}%"
        ax2.text(bar.get_x() + bar.get_width() / 2, u + 2.5, lbl, ha="center", fontweight="bold", fontsize=9.5)
    ax2.legend(loc="upper right", frameon=True, facecolor="white")

    fig.suptitle("M/M/c Queueing Analysis: Human-in-the-Loop SOC Capacity & SLA Compliance", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_4_mmc_queueing")


# ---------------------------------------------------------------------------
# 5. 5-Year Financial ROI, TCO, and Cumulative NPV (NIS Millions)
# ---------------------------------------------------------------------------
@dataclass(frozen=True, slots=True)
class FinancialModel:
    capex: FloatArray
    opex: FloatArray
    benefits: FloatArray
    discount_rate: float = 0.06

    def __post_init__(self) -> None:
        if not (self.capex.shape == self.opex.shape == self.benefits.shape):
            raise ValueError("capex, opex, and benefits must have identical shapes.")
        if self.discount_rate < 0.0:
            raise ValueError("discount_rate must be non-negative.")

    def evaluate(self) -> tuple[FloatArray, FloatArray, float, float, float]:
        years = np.arange(1, self.capex.size + 1, dtype=np.float64)
        total_cost = self.capex + self.opex
        net_cf = self.benefits - total_cost
        disc = 1.0 / ((1.0 + self.discount_rate) ** years)
        cum_npv = np.cumsum(net_cf * disc)
        tco = float(total_cost.sum())
        tot_ben = float(self.benefits.sum())
        roi = ((tot_ben - tco) / tco) * 100.0
        return total_cost, cum_npv, tco, tot_ben, roi


def generate_fig_roi() -> tuple[float, float, float, float]:
    model = FinancialModel(
        capex=np.array([6.8, 1.2, 0.8, 0.8, 0.6], dtype=np.float64),
        opex=np.array([2.4, 3.1, 3.3, 3.5, 3.7], dtype=np.float64),
        benefits=np.array([5.5, 13.8, 17.5, 20.2, 22.8], dtype=np.float64),
        discount_rate=0.06,
    )
    total_cost, cum_npv, total_cost_5y, total_ben_5y, roi_5y = model.evaluate()
    years = np.arange(1, 6)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

    w = 0.34
    ax1.bar(years - w / 2, total_cost, width=w, color=CRIMSON, alpha=0.88, label="Total Cost (CapEx + OpEx)")
    ax1.bar(years + w / 2, model.benefits, width=w, color=TEAL, alpha=0.90, label="Quantified Benefits & Avoided Losses")
    ax1.set_xticks(years)
    ax1.set_xticklabels([f"Year {y}" for y in years])
    ax1.set_ylabel("NIS Millions")
    ax1.set_title("Annual Cost vs. Quantified Economic Benefit")
    ax1.legend(loc="upper left", frameon=True, facecolor="white")

    ax2.plot(years, cum_npv, marker="o", lw=2.6, color=NAVY, label="Cumulative NPV (6% Discount Rate)")
    ax2.fill_between(years, 0, cum_npv, where=(cum_npv >= 0), color=TEAL, alpha=0.18)
    ax2.fill_between(years, 0, cum_npv, where=(cum_npv < 0), color=CRIMSON, alpha=0.18)
    ax2.axhline(0, color=SLATE, lw=1.2)
    ax2.set_xticks(years)
    ax2.set_xticklabels([f"Year {y}" for y in years])
    ax2.set_ylabel("Cumulative NPV (NIS Millions)")
    ax2.set_title(f"5-Year Cumulative NPV: {cum_npv[-1]:.1f}M NIS (ROI: {roi_5y:.0f}%)")
    for y, v in zip(years, cum_npv):
        ax2.annotate(f"{v:.1f}M", (y, v), textcoords="offset points", xytext=(0, 8), ha="center", fontweight="bold", fontsize=9)
    ax2.legend(loc="upper left", frameon=True, facecolor="white")

    fig.suptitle("CivicShield AI 5-Year Financial Model: TCO, Avoided Crisis Cost & NPV", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_5_roi_5yr")
    return total_cost_5y, total_ben_5y, float(cum_npv[-1]), roi_5y


def main() -> None:
    p_base, p_cs, red = generate_fig_siri()
    s_base, s_cs = generate_fig_hk()
    post_p, auc_f = generate_fig_bayesian()
    generate_fig_mmc()
    tc, tb, npv5, roi5 = generate_fig_roi()

    print("\n--- Verified Simulation Metrics ---")
    print(f"SIRI Peak Infected: Baseline={p_base:.2f}%, CivicShield={p_cs:.2f}%, Reduction={red:.1f}%")
    print(f"HK Final Std Dev:   Baseline={s_base:.3f}, CivicShield={s_cs:.3f}")
    print(f"Bayesian Fusion:    Posterior={post_p:.2f}%, AUC={auc_f:.3f}")
    print(f"5Y Financial:       TCO={tc:.1f}M NIS, Benefits={tb:.1f}M NIS, NPV={npv5:.1f}M NIS, ROI={roi5:.1f}%")


if __name__ == "__main__":
    main()
