import pandas as pd
import numpy as np
import os
import time
import json
from sklearn.metrics import mean_squared_error, roc_auc_score, brier_score_loss

# Imports for models
from src.infrastructure.adapters.models.baseline_models import (
    MeanImputation,
    LOCFImputation,
)
from src.infrastructure.adapters.models.ssm_wrapper import SSMImputeWrapper
from src.infrastructure.adapters.models.dsc_model import DSCMethod
from src.infrastructure.simulation.generate_sdpc_2026 import generate_sdpc_2026


def kl_divergence(p, q):
    p = np.clip(p, 1e-10, 1.0)
    q = np.clip(q, 1e-10, 1.0)
    return p * np.log(p / q) + (1 - p) * np.log((1 - p) / (1 - q))


def entropy(p):
    p = np.clip(p, 1e-10, 1.0)
    return -p * np.log(p) - (1 - p) * np.log(1 - p)


def calculate_advanced_metrics(df_true, df_pred):
    """
    Calculates Causal Calibration (CC) and Intervention Integrity (II).
    CC: Measures how well the imputation recovers the hidden ground truth Y*.
    II: Measures how well the predicted missingness probability matches the true P(M|S).
    """
    mask = df_true["M"] == 1
    if mask.sum() == 0:
        return 0.0, 0.0

    # CC: RMSE on Y_star for missing points (Lower is better)
    cc = np.sqrt(
        mean_squared_error(df_true.loc[mask, "Y_star"], df_pred.loc[mask, "Y_imputed"])
    )

    # II: 1 - DKL(Preal || Psyn) / Hreal
    # True P(M|S) from the simulator parameters
    beta_0 = -1.0
    beta_s = -3.0
    s_true = df_true["S_true"].values
    logits_real = beta_0 + beta_s * (s_true - 0.5)
    p_real = 1 / (1 + np.exp(-logits_real))

    if "M_prob" in df_pred.columns:
        p_syn = df_pred["M_prob"].values
        dkl = np.mean(kl_divergence(p_real, p_syn))
        h_real = np.mean(entropy(p_real))
        # Clip II to [0, 1]
        ii = max(0.0, 1 - (dkl / (h_real + 1e-6)))
    else:
        ii = 0.0

    return float(cc), float(ii)


def calculate_metrics(df_true, df_pred, threshold=0.2):
    """
    Calculate RMSE, T-AUROC, and Brier Score for hidden values.
    """
    mask = df_true["M"] == 1
    if mask.sum() == 0:
        return 0.0, 0.5, 0.0

    y_true_hidden = df_true.loc[mask, "Y_star"]
    y_pred_hidden = df_pred.loc[mask, "Y_imputed"]

    # RMSE
    rmse = np.sqrt(mean_squared_error(y_true_hidden, y_pred_hidden))

    # Clinical Crisis Detection (Binary)
    # Crisis is defined by low latent state S_true
    labels = (df_true.loc[mask, "S_true"] < threshold).astype(int)
    # Model scores: lower Y_imputed should mean higher risk of crisis
    scores = -df_pred.loc[mask, "Y_imputed"]

    # AUROC
    try:
        auroc = roc_auc_score(labels, scores)
    except Exception:
        auroc = 0.5

    # Brier Score (using a simple mapping of Y_imputed to probability)
    # This is a proxy for the probability of crisis
    probs = 1 / (1 + np.exp(df_pred.loc[mask, "Y_imputed"] - 0.5))
    brier = brier_score_loss(labels, probs)

    return float(rmse), float(auroc), float(brier)


def run_benchmarks():
    print("Initializing Scaled Clinical Benchmarking...")
    os.makedirs("results", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    # Scaled Certification Set: N=1000 patients, 60-day windows
    print("Generating Certification Set (N=1000 patients, 60 days)...")
    df_train = generate_sdpc_2026(n_patients=800, n_days=60, seed=42)
    df_test = generate_sdpc_2026(n_patients=200, n_days=60, seed=123)

    models = {
        "Mean": MeanImputation(),
        "LOCF": LOCFImputation(),
        "SSMimpute": SSMImputeWrapper(),
        "DSC-Method (Upgraded)": DSCMethod(epochs=30, causal_lambda=2.0),
    }

    all_results = []

    for name, model in models.items():
        print(f"\n--- Method: {name} ---")
        start_time = time.time()

        # Train
        model.fit(df_train)
        train_duration = time.time() - start_time

        # Predict
        inf_start = time.time()
        df_pred = model.predict(df_test)
        inference_duration = time.time() - inf_start

        # Evaluate
        rmse, auroc, brier = calculate_metrics(df_test, df_pred)
        cc, ii = calculate_advanced_metrics(df_test, df_pred)

        result = {
            "Method": name,
            "RMSE": rmse,
            "T-AUROC": auroc,
            "Brier": brier,
            "CausalCalibration": cc,
            "InterventionIntegrity": ii,
            "TrainTime": train_duration,
            "InferenceTime": inference_duration,
        }
        all_results.append(result)

        print(
            f"[{name}] RMSE: {rmse:.4f}, AUROC: {auroc:.4f}, CC: {cc:.4f}, II: {ii:.4f}"
        )

        # Save predictions for the visualization script
        if name == "DSC-Method (Upgraded)":
            df_pred.to_csv("data/dsc_test_predictions.csv", index=False)
        elif name == "LOCF":
            df_pred.to_csv("data/locf_test_predictions.csv", index=False)
        elif name == "SSMimpute":
            df_pred.to_csv("data/ssm_test_predictions.csv", index=False)

    # Save Ground Truth for visualization
    df_test.to_csv("data/test_ground_truth.csv", index=False)

    # Save Results
    results_df = pd.DataFrame(all_results)
    results_df.to_csv("results/benchmark_metrics_all.csv", index=False)

    with open("results/certification_summary.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print(
        "\nBenchmarking Complete. Scaled results saved to results/benchmark_metrics_all.csv"
    )


if __name__ == "__main__":
    run_benchmarks()
