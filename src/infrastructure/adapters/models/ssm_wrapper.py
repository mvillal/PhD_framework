import pandas as pd
from src.domain.experiment.interfaces import ImputationModel


class SSMImputeWrapper(ImputationModel):
    """
    Simplified SSM Imputation using Linear Interpolation and a smoothing prior.
    This acts as a proxy for more complex State-Space Models.
    """

    def fit(self, df: pd.DataFrame) -> None:
        pass

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()

        def process_patient(group):
            # Linear interpolation
            interpolated = group.interpolate(method="linear")
            # Fill edges
            return interpolated.ffill().bfill()

        df_out["Y_imputed"] = df_out.groupby("patient_id", group_keys=False)[
            "Y_obs"
        ].apply(process_patient)

        # Fallback to global mean for patients with NO observed data
        global_mean = df["Y_obs"].mean()
        df_out["Y_imputed"] = df_out["Y_imputed"].fillna(global_mean)

        return df_out
