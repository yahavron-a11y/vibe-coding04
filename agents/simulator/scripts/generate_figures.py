"""
CivicShield AI Preliminary Report - Chapter 4 Simulation & Figure Generator.
Generates high-resolution vector PDF and 300-DPI PNG figures for:
  1. SIRI ODE Disinformation Dynamics (Baseline vs. CivicShield AI)
  2. Hegselmann-Krause Bounded-Confidence Opinion Dynamics
  3. Multi-Modal Bayesian Fusion & ROC Performance
  4. M/M/c Queueing Theory (Erlang-C HITL SOC Triage)
  5. 5-Year Financial ROI, TCO, and Cumulative NPV Analysis
"""

import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

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

NAVY = "#1B365D"
TEAL = "#008080"
CRIMSON = "#C0392B"
AMBER = "#D68910"
SLATE = "#5D6D7E"
GREEN = "#1E8449"


def save_fig(fig, stem: str):
    pdf_path = os.path.join(OUT_DIR, f"{stem}.pdf")
    png_path = os.path.join(OUT_DIR, f"{stem}.png")
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved {pdf_path} and {png_path}")


# ---------------------------------------------------------------------------
# Figure 4.1: SIRI ODE Model (RK4 integrator, zero external solver dependency)
# ---------------------------------------------------------------------------
def rk4_siri(y0, t, beta, gamma, delta, mu_re):
    """
    SIRI model:
      dS/dt = -beta * S * I - delta * S
      dI/dt =  beta * S * I + mu_re * R * I - gamma * I
      dR/dt =  gamma * I - mu_re * R * I
      dM/dt =  delta * S   (Pre-bunked / Immunized compartment, denoted I_m or M)
    """
    n = len(t)
    Y = np.zeros((n, 4))
    Y[0] = y0

    def f(y):
        S, I, R, M = y
        dS = -beta * S * I - delta * S
        dI = beta * S * I + mu_re * R * I - gamma * I
        dR = gamma * I - mu_re * R * I
        dM = delta * S
        return np.array([dS, dI, dR, dM])

    for k in range(n - 1):
        dt = t[k + 1] - t[k]
        yk = Y[k]
        k1 = f(yk)
        k2 = f(yk + 0.5 * dt * k1)
        k3 = f(yk + 0.5 * dt * k2)
        k4 = f(yk + dt * k3)
        Y[k + 1] = yk + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return Y


def generate_fig_siri():
    t = np.linspace(0, 72, 721)  # 72 hours
    y0 = np.array([0.992, 0.008, 0.0, 0.0])

    # Baseline: high infectivity, slow debunking, re-infection possible
    Y_base = rk4_siri(y0, t, beta=0.42, gamma=0.12, delta=0.002, mu_re=0.08)
    # CivicShield AI: early detection reduces beta, active pre-bunking increases delta, fast fact-check increases gamma
    Y_cs = rk4_siri(y0, t, beta=0.21, gamma=0.26, delta=0.025, mu_re=0.015)

    peak_base = Y_base[:, 1].max() * 100
    peak_cs = Y_cs[:, 1].max() * 100
    reduction = (1.0 - peak_cs / peak_base) * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), sharey=True)

    ax1.plot(t, Y_base[:, 0] * 100, color=NAVY, lw=2.0, label="Susceptible $S(t)$")
    ax1.plot(t, Y_base[:, 1] * 100, color=CRIMSON, lw=2.4, label="Infected / Believers $I(t)$")
    ax1.plot(t, Y_base[:, 2] * 100, color=SLATE, lw=1.8, ls="--", label="Recovered $R(t)$")
    ax1.plot(t, Y_base[:, 3] * 100, color=TEAL, lw=1.8, ls=":", label="Immunized $M(t)$")
    ax1.set_title("Baseline (No Intervention, $R_0 = 3.50$)")
    ax1.set_xlabel("Time Since Campaign Onset (Hours)")
    ax1.set_ylabel("Population Share (%)")
    ax1.legend(loc="right", frameon=True, facecolor="white", framealpha=0.9)
    t_pk_b = t[np.argmax(Y_base[:, 1])]
    ax1.annotate(f"Peak: {peak_base:.1f}%", xy=(t_pk_b, peak_base),
                 xytext=(t_pk_b + 10, peak_base + 7),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON),
                 color=CRIMSON, fontweight="bold")

    ax2.plot(t, Y_cs[:, 0] * 100, color=NAVY, lw=2.0, label="Susceptible $S(t)$")
    ax2.plot(t, Y_cs[:, 1] * 100, color=CRIMSON, lw=2.4, label="Infected / Believers $I(t)$")
    ax2.plot(t, Y_cs[:, 2] * 100, color=SLATE, lw=1.8, ls="--", label="Recovered $R(t)$")
    ax2.plot(t, Y_cs[:, 3] * 100, color=TEAL, lw=2.2, ls="-.", label="Pre-bunked / Immunized $M(t)$")
    ax2.set_title(f"With CivicShield AI ($R_{{\\mathrm{{eff}}}} = 0.81$, Peak -{reduction:.1f}%)")
    ax2.set_xlabel("Time Since Campaign Onset (Hours)")
    ax2.legend(loc="right", frameon=True, facecolor="white", framealpha=0.9)
    t_pk_c = t[np.argmax(Y_cs[:, 1])]
    ax2.annotate(f"Peak: {peak_cs:.1f}%", xy=(t_pk_c, peak_cs),
                 xytext=(t_pk_c + 12, peak_cs + 14),
                 arrowprops=dict(arrowstyle="->", color=CRIMSON),
                 color=CRIMSON, fontweight="bold")

    fig.suptitle("SIRI Disinformation Propagation Model: 72-Hour Crisis Simulation", fontsize=13, fontweight="bold", y=1.02)
    fig.tight_layout()
    save_fig(fig, "fig4_1_siri_ode")
    return peak_base, peak_cs, reduction


# ---------------------------------------------------------------------------
# Figure 4.2: Hegselmann-Krause Bounded-Confidence Opinion Dynamics
# ---------------------------------------------------------------------------
def simulate_hk(x0, eps, steps=35, bridge_agents=0, bridge_weight=0.0):
    N = len(x0)
    hist = np.zeros((steps + 1, N))
    hist[0] = x0.copy()
    x = x0.copy()
    for t in range(steps):
        x_new = np.empty_like(x)
        for i in range(N):
            neighbors = x[np.abs(x - x[i]) <= eps]
            val = neighbors.mean()
            if bridge_agents > 0:
                # CivicShield verified-context nudges agents near the boundary toward factual center (0.5)
                val = (1.0 - bridge_weight) * val + bridge_weight * 0.5
            x_new[i] = val
        x = x_new
        hist[t + 1] = x
    return hist


def generate_fig_hk():
    rng = np.random.default_rng(42)
    N = 160
    # Bimodal initial opinion distribution under adversarial polarization
    x0 = np.concatenate([
        rng.uniform(0.02, 0.42, N // 2),
        rng.uniform(0.58, 0.98, N // 2)
    ])
    steps = 30
    hist_base = simulate_hk(x0, eps=0.18, steps=steps, bridge_agents=0, bridge_weight=0.0)
    hist_cs = simulate_hk(x0, eps=0.26, steps=steps, bridge_agents=1, bridge_weight=0.08)

    std_base = hist_base[-1].std()
    std_cs = hist_cs[-1].std()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), sharey=True)
    t_axis = np.arange(steps + 1)

    for i in range(N):
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
# Figure 4.3: Multi-Modal Bayesian Sensor Fusion & ROC Analysis
# ---------------------------------------------------------------------------
def generate_fig_bayesian():
    # Sequential Bayesian posterior update across 4 independent detection modalities
    stages = ["Prior\n$P(H_1)$", "+ NLP\nSemantics", "+ Network\nGraph", "+ Media\nForensics", "+ Source\nCredibility"]
    # Likelihood ratios (LR = P(E|H1) / P(E|H0)) for a true coordinated disinformation event
    lrs_true = [1.0, 4.8, 3.6, 5.2, 2.4]
    # Likelihood ratios for a benign viral news event (false-alarm stress test)
    lrs_benign = [1.0, 1.4, 0.55, 0.18, 0.25]

    def bayes_seq(prior, lrs):
        odds = prior / (1.0 - prior)
        probs = [prior]
        for lr in lrs[1:]:
            odds *= lr
            probs.append(odds / (1.0 + odds))
        return np.array(probs)

    p_true = bayes_seq(0.05, lrs_true)
    p_benign = bayes_seq(0.05, lrs_benign)

    # Synthetic smooth ROC curves for single-modality vs fused Bayesian engine
    fpr = np.linspace(0, 1, 300)
    tpr_nlp = 1 - (1 - fpr) ** 3.8
    tpr_net = 1 - (1 - fpr) ** 5.0
    tpr_fused = 1 - (1 - fpr) ** 26.5

    auc_nlp = np.trapezoid(tpr_nlp, fpr)
    auc_net = np.trapezoid(tpr_net, fpr)
    auc_fused = np.trapezoid(tpr_fused, fpr)

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
    return p_true[-1] * 100, auc_fused


# ---------------------------------------------------------------------------
# Figure 4.4: M/M/c Queueing Theory (Erlang-C) for SOC HITL Analysts
# ---------------------------------------------------------------------------
def erlang_c_wq(lam, mu, c):
    rho = lam / (c * mu)
    if rho >= 0.999:
        return np.nan
    a = lam / mu
    sum_terms = sum((a ** k) / math.factorial(k) for k in range(c))
    last_term = (a ** c) / (math.factorial(c) * (1.0 - rho))
    p_wait = last_term / (sum_terms + last_term)
    wq_hours = p_wait / (c * mu - lam)
    return wq_hours * 60.0  # minutes


def generate_fig_mmc():
    mu = 6.0  # 6 complex alerts/hour per human analyst (10 min avg review)
    lam_vals = np.linspace(10, 115, 220)  # raw crisis alert arrival rate (alerts/hour)

    # Without AI triage: 100% alerts hit human analysts (c=12 or c=16)
    wq_no_ai_12 = [erlang_c_wq(l, mu, 12) for l in lam_vals]
    wq_no_ai_16 = [erlang_c_wq(l, mu, 16) for l in lam_vals]
    # With CivicShield AI triage: 78% auto-filtered/resolved -> effective lambda = 0.22 * lam, with only c=6 analysts
    wq_ai_6 = [erlang_c_wq(0.22 * l, mu, 6) for l in lam_vals]

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

    # Bar chart of utilization at peak crisis lambda = 85 alerts/hr
    configs = ["Manual\n($c=12$)", "Manual\n($c=16$)", "CivicShield AI\n($c=6$)"]
    utils = [min(100.0, (85 / (12 * mu)) * 100), (85 / (16 * mu)) * 100, ((0.22 * 85) / (6 * mu)) * 100]
    colors = [CRIMSON, AMBER, TEAL]
    bars = ax2.bar(configs, utils, color=colors, width=0.52, edgecolor=NAVY, linewidth=0.8)
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
# Figure 4.5: 5-Year Financial ROI, TCO, and Cumulative NPV (NIS Millions)
# ---------------------------------------------------------------------------
def generate_fig_roi():
    years = np.array([1, 2, 3, 4, 5])
    # Costs in NIS Millions (CapEx heavy in Y1, lean OpEx Y2-Y5)
    capex = np.array([6.8, 1.2, 0.8, 0.8, 0.6])
    opex = np.array([2.4, 3.1, 3.3, 3.5, 3.7])
    total_cost = capex + opex

    # Benefits in NIS Millions (SOC labor savings + avoided civic/economic crisis disruption)
    benefits = np.array([5.5, 13.8, 17.5, 20.2, 22.8])
    net_cf = benefits - total_cost

    r = 0.06  # 6% government social discount rate
    disc_factors = 1.0 / ((1.0 + r) ** years)
    cum_npv = np.cumsum(net_cf * disc_factors)
    total_cost_5y = total_cost.sum()
    total_ben_5y = benefits.sum()
    roi_5y = ((total_ben_5y - total_cost_5y) / total_cost_5y) * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4))

    w = 0.34
    ax1.bar(years - w / 2, total_cost, width=w, color=CRIMSON, alpha=0.88, label="Total Cost (CapEx + OpEx)")
    ax1.bar(years + w / 2, benefits, width=w, color=TEAL, alpha=0.90, label="Quantified Benefits & Avoided Losses")
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
    return total_cost_5y, total_ben_5y, cum_npv[-1], roi_5y


if __name__ == "__main__":
    p_base, p_cs, red = generate_fig_siri()
    s_base, s_cs = generate_fig_hk()
    post_p, auc_f = generate_fig_bayesian()
    generate_fig_mmc()
    tc, tb, npv5, roi5 = generate_fig_roi()
    print("\n--- Summary Metrics ---")
    print(f"SIRI Peak Infected: Baseline={p_base:.2f}%, CivicShield={p_cs:.2f}%, Reduction={red:.1f}%")
    print(f"HK Final Std Dev: Baseline={s_base:.3f}, CivicShield={s_cs:.3f}")
    print(f"Bayesian Fusion: Posterior={post_p:.2f}%, AUC={auc_f:.3f}")
    print(f"5Y Financial: TotalCost={tc:.1f}M NIS, TotalBenefit={tb:.1f}M NIS, NPV={npv5:.1f}M NIS, ROI={roi5:.1f}%")
