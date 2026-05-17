import pandas as pd
from src.domain.experiment.interfaces import ImputationModel


class MeanImputation(ImputationModel):
    def __init__(self):
        self.mean_val = 0.0

    def fit(self, df: pd.DataFrame) -> None:
        self.mean_val = df["Y_obs"].mean()

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        df_out["Y_imputed"] = df_out["Y_obs"].fillna(self.mean_val)
        return df_out


class LOCFImputation(ImputationModel):
    def fit(self, df: pd.DataFrame) -> None:
        pass

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        df_out = df.copy()
        # Group by patient_id and forward fill
        df_out["Y_imputed"] = df_out.groupby("patient_id", group_keys=False)[
            "Y_obs"
        ].apply(lambda x: x.ffill())
        # For remaining NaNs at the beginning of trajectory, use global mean
        global_mean = df["Y_obs"].mean()
        df_out["Y_imputed"] = df_out["Y_imputed"].fillna(global_mean)
        return df_out
