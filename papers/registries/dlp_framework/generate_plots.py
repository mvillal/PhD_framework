import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Set publication style for clinical journals
sns.set_theme(style="whitegrid", context="paper")
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 14,
        "legend.fontsize": 10,
        "figure.dpi": 300,
        "text.usetex": False,  # Keep false for environment compatibility
    }
)


def plot_trajectories():
    if not os.path.exists("data/dsc_test_predictions.csv") or not os.path.exists(
        "data/test_ground_truth.csv"
    ):
        print("Data files not found. Run benchmarks first.")
        return

    df_pred = pd.read_csv("data/dsc_test_predictions.csv")
    df_true = pd.read_csv("data/test_ground_truth.csv")

    # Calculate patient-wise RMSE on missing points to find best/worst
    patient_rmses = {}
    patients = df_true["patient_id"].unique()
    for p in patients:
        p_true = df_true[df_true["patient_id"] == p]
        p_pred = df_pred[df_pred["patient_id"] == p]
        mask = p_true["M"] == 1
        if mask.sum() > 0:
            rmse = np.sqrt(
                (
                    (p_true.loc[mask, "Y_star"] - p_pred.loc[mask, "Y_imputed"]) ** 2
                ).mean()
            )
            patient_rmses[p] = rmse

    if not patient_rmses:
        print("No missing points found to plot.")
        return

    # Automatically identify best and worst recovery trajectories
    best_p = min(patient_rmses, key=patient_rmses.get)
    worst_p = max(patient_rmses, key=patient_rmses.get)

    print(f"Best Patient: {best_p} (RMSE: {patient_rmses[best_p]:.4f})")
    print(f"Worst Patient: {worst_p} (RMSE: {patient_rmses[worst_p]:.4f})")

    os.makedirs("plots", exist_ok=True)

    for p_id, label in [(best_p, "Best_Recovery"), (worst_p, "Worst_Recovery")]:
        p_true = df_true[df_true["patient_id"] == p_id]
        p_pred = df_pred[df_pred["patient_id"] == p_id]

        fig, (ax1, ax2) = plt.subplots(
            2, 1, figsize=(10, 8), gridspec_kw={"height_ratios": [3, 1]}, sharex=True
        )

        # Main Trajectory Plot
        ax1.plot(
            p_true["time"],
            p_true["S_true"],
            color="black",
            linestyle="--",
            linewidth=1.0,
            label="Latent State $S_t$ (Truth)",
        )
        ax1.plot(
            p_true["time"],
            p_true["Y_star"],
            color="gray",
            linestyle=":",
            linewidth=0.8,
            alpha=0.5,
            label="True Behavior $Y^*$",
        )

        obs_mask = p_true["M"] == 0
        ax1.scatter(
            p_true.loc[obs_mask, "time"],
            p_true.loc[obs_mask, "Y_obs"],
            color="#1f77b4",
            s=25,
            label="Observed Sensor Data",
            zorder=5,
        )

        miss_mask = p_true["M"] == 1
        ax1.scatter(
            p_true.loc[miss_mask, "time"],
            p_pred.loc[miss_mask, "Y_imputed"],
            color="#d62728",
            marker="x",
            s=40,
            label="DSC Recovery",
            zorder=5,
        )

        # Highlight persistent dropout windows
        if miss_mask.any():
            m_indices = np.where(miss_mask)[0]
            if len(m_indices) > 0:
                start = m_indices[0]
                for i in range(1, len(m_indices)):
                    if m_indices[i] != m_indices[i - 1] + 1:
                        ax1.axvspan(
                            p_true.iloc[start]["time"],
                            p_true.iloc[m_indices[i - 1]]["time"],
                            color="yellow",
                            alpha=0.1,
                        )
                        start = m_indices[i]
                ax1.axvspan(
                    p_true.iloc[start]["time"],
                    p_true.iloc[m_indices[-1]]["time"],
                    color="yellow",
                    alpha=0.1,
                    label="Persistent Dropout",
                )

        ax1.set_title(f"Clinical Signal Recovery ({label}) - Patient {p_id}")
        ax1.set_ylabel("Standardized Clinical State")
        ax1.legend(loc="best", frameon=True)

        # Residual Plot
        residuals = p_true.loc[miss_mask, "Y_star"] - p_pred.loc[miss_mask, "Y_imputed"]
        ax2.scatter(
            p_true.loc[miss_mask, "time"],
            residuals,
            color="purple",
            marker="o",
            s=20,
            alpha=0.6,
        )
        ax2.axhline(0, color="black", linestyle="-", linewidth=0.5)
        ax2.set_ylabel("Residual")
        ax2.set_xlabel("Time (Days)")

        sns.despine()
        plt.tight_layout()
        plt.savefig(f"plots/trajectory_{label.lower()}.png")
        print(f"Saved {label} plot.")

    # Generate Residual Heatmap
    plot_residual_heatmap(df_true, df_pred)

    # Generate Comparison Plot
    if os.path.exists("data/locf_test_predictions.csv") and os.path.exists(
        "data/ssm_test_predictions.csv"
    ):
        df_locf = pd.read_csv("data/locf_test_predictions.csv")
        df_ssm = pd.read_csv("data/ssm_test_predictions.csv")
        plot_comparison(df_true, df_pred, df_locf, df_ssm)


def plot_residual_heatmap(df_true, df_pred):
    print("Generating Residual Heatmap...")
    # Sample 200 patients for the heatmap
    all_patients = sorted(df_true["patient_id"].unique())
    patients = all_patients[:200]
    times = sorted(df_true["time"].unique())

    heatmap_data = np.full((len(patients), len(times)), np.nan)

    for i, p in enumerate(patients):
        p_true = df_true[df_true["patient_id"] == p]
        p_pred = df_pred[df_pred["patient_id"] == p]

        mask = p_true["M"] == 1
        if mask.any():
            # Merge true and pred on time to ensure alignment
            merged = pd.merge(
                p_true.loc[mask, ["time", "Y_star"]],
                p_pred.loc[mask, ["time", "Y_imputed"]],
                on="time",
            )
            for _, row in merged.iterrows():
                t_idx = np.searchsorted(times, row["time"])
                heatmap_data[i, t_idx] = row["Y_star"] - row["Y_imputed"]

    plt.figure(figsize=(12, 10))
    # Use RdBu_r so red is overestimation and blue is underestimation (or vice versa)
    sns.heatmap(
        heatmap_data,
        cmap="RdBu_r",
        center=0,
        cbar_kws={"label": "Residual Error (Truth - Imputed)"},
    )
    plt.title("Spatiotemporal Error Distribution (Residual Heatmap)")
    plt.xlabel("Time (Days)")
    plt.ylabel("Patient Index (Test Set)")
    plt.savefig("plots/residual_heatmap.png")
    print("Saved plots/residual_heatmap.png")


def plot_comparison(df_true, df_dsc, df_locf, df_ssm):
    print("Generating Detailed Method Comparison...")
    # Find a patient with a "crisis" (sharp drop in S_true) and significant missingness
    # A crisis is defined as S_true < 0.2
    crisis_patients = df_true[df_true["S_true"] < 0.2]["patient_id"].unique()

    target_p = None
    for p in crisis_patients:
        p_true = df_true[df_true["patient_id"] == p]
        # Check if they have missingness during the crisis
        crisis_missing = p_true[(p_true["S_true"] < 0.2) & (p_true["M"] == 1)]
        if len(crisis_missing) > 3:
            target_p = p
            break

    if target_p is None:
        target_p = df_true["patient_id"].unique()[0]

    p_true = df_true[df_true["patient_id"] == target_p]
    p_dsc = df_dsc[df_dsc["patient_id"] == target_p]
    p_locf = df_locf[df_locf["patient_id"] == target_p]
    p_ssm = df_ssm[df_ssm["patient_id"] == target_p]

    plt.figure(figsize=(10, 6))
    plt.plot(
        p_true["time"], p_true["Y_star"], "k--", label="Ground Truth $Y^*$", alpha=0.4
    )

    obs_mask = p_true["M"] == 0
    plt.scatter(
        p_true.loc[obs_mask, "time"],
        p_true.loc[obs_mask, "Y_obs"],
        c="black",
        s=30,
        label="Observed Data",
        edgecolors="white",
        zorder=10,
    )

    miss_mask = p_true["M"] == 1
    # Sort by time for clean lines
    t_miss = p_true.loc[miss_mask, "time"]
    plt.plot(
        t_miss,
        p_dsc.loc[miss_mask, "Y_imputed"],
        "r-o",
        markersize=5,
        label="DSC (Our Latent SDE)",
        linewidth=2,
    )
    plt.plot(
        t_miss,
        p_ssm.loc[miss_mask, "Y_imputed"],
        "g-^",
        markersize=5,
        label="SSMimpute (State Space)",
        alpha=0.7,
    )
    plt.plot(
        t_miss,
        p_locf.loc[miss_mask, "Y_imputed"],
        "b-s",
        markersize=5,
        label="LOCF (Baseline)",
        alpha=0.5,
    )

    # Highlight crisis region
    plt.axvspan(
        t_miss.min(),
        t_miss.max(),
        color="red",
        alpha=0.05,
        label="Disengagement Window",
    )

    plt.title(f"Method Comparison: Recovery of Crisis Trajectory (Patient {target_p})")
    plt.xlabel("Time (Days)")
    plt.ylabel("Standardized Symptom Score")
    plt.legend(loc="best", frameon=True)
    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/method_comparison_detail.png")
    print("Saved plots/method_comparison_detail.png")


def plot_benchmarks():
    results_path = "results/benchmark_metrics_all.csv"
    if not os.path.exists(results_path):
        return

    df = pd.read_csv(results_path)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # T-AUROC Plot
    sns.barplot(data=df, x="Method", y="T-AUROC", ax=ax1, palette="viridis")
    ax1.axhline(
        0.8, color="red", linestyle=":", alpha=0.6, label="Clinical Utility Floor"
    )
    ax1.set_title("Predictive Utility (T-AUROC)")
    ax1.set_ylim(0.4, 1.0)
    ax1.tick_params(axis="x", rotation=45)

    # Causal Calibration vs Intervention Integrity
    # Good models should be top-right
    sns.scatterplot(
        data=df,
        x="InterventionIntegrity",
        y="CausalCalibration",
        hue="Method",
        s=100,
        ax=ax2,
        style="Method",
    )
    ax2.set_title("Causal Robustness Trade-off")
    ax2.set_ylabel(
        r"Causal Calibration (RMSE $\downarrow$)"
    )  # Note: lower is better for RMSE-based CC
    ax2.set_xlabel(r"Intervention Integrity (II $\uparrow$)")

    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/benchmark_comparison.png")
    print("Saved benchmark comparison plot.")


if __name__ == "__main__":
    plot_trajectories()
    plot_benchmarks()
