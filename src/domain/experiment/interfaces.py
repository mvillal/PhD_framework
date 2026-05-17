from abc import ABC, abstractmethod
import pandas as pd


class ImputationModel(ABC):
    @abstractmethod
    def fit(self, df: pd.DataFrame) -> None:
        """Fit the model to the training data."""
        pass

    @abstractmethod
    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Predict/Impute missing values.
        Returns the dataframe with an additional column 'Y_imputed'.
        """
        pass
