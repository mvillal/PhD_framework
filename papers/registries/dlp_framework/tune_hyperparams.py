import pandas as pd
import numpy as np
import os
from src.infrastructure.adapters.models.dsc_sde import DSCSDE
from src.infrastructure.adapters.models.dsc_transformer import DSCTransformer
from sklearn.metrics import mean_squared_error


def tune():
    data_path = "data/sdpc_2026_synthetic.csv"
    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}. Please run simulation first.")
        return

    df = pd.read_csv(data_path)
    patients = df["patient_id"].unique()
    # Split patients for train/val
    np.random.shuffle(patients)
    train_patients = patients[:800]
    val_patients = patients[800:]

    train_df = df[df["patient_id"].isin(train_patients)]
    val_df = df[df["patient_id"].isin(val_patients)]

    latent_dims = [16, 32, 64]
    learning_rates = [1e-4, 1e-3]

    results = []

    os.makedirs("results", exist_ok=True)

    for model_class in [DSCSDE, DSCTransformer]:
        for ld in latent_dims:
            for lr in learning_rates:
                print(
                    f"\n--- Testing {model_class.__name__} with latent_dim={ld}, lr={lr} ---"
                )
                # Reduced epochs for faster tuning in this phase
                model = model_class(epochs=30, lr=lr, latent_dim=ld)
                model.fit(train_df)

                pred_df = model.predict(val_df)
                # Calculate MSE on missing values using Y_star (ground truth without missingness but with noise)
                mask = val_df["Y_obs"].isna()
                if mask.any():
                    mse = mean_squared_error(
                        val_df.loc[mask, "Y_star"], pred_df.loc[mask, "Y_imputed"]
                    )
                    results.append(
                        {
                            "model": model_class.__name__,
                            "latent_dim": ld,
                            "lr": lr,
                            "mse": mse,
                        }
                    )
                    print(f"Validation MSE: {mse:.4f}")
                else:
                    print("No missing values in validation set to evaluate.")

    results_df = pd.DataFrame(results)
    results_df.to_csv("results/hyperparam_tuning.csv", index=False)
    print("\nTuning complete. Results saved to results/hyperparam_tuning.csv")


if __name__ == "__main__":
    tune()
