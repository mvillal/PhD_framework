from abc import ABC, abstractmethod
from typing import Optional
from src.domain.experiment.entities import Run, Metric, Parameter, Step, Artifact


class ExperimentTrackerPort(ABC):
    @abstractmethod
    def start_run(self, run: Run) -> None:
        """Initialize a run in the tracking backend."""
        pass

    @abstractmethod
    def log_metric(self, run_id: str, metric: Metric) -> None:
        """Log a single metric to the tracking backend."""
        pass

    @abstractmethod
    def log_parameter(self, run_id: str, parameter: Parameter) -> None:
        """Log a single parameter to the tracking backend."""
        pass

    @abstractmethod
    def log_step(self, run_id: str, step: Step) -> None:
        """Log an agent step with explanation."""
        pass

    @abstractmethod
    def log_artifact(self, run_id: str, artifact: Artifact) -> None:
        """Log a text or file artifact."""
        pass

    @abstractmethod
    def end_run(self, run_id: str, status: str) -> None:
        """Finalize a run in the tracking backend."""
        pass


class RunRepositoryPort(ABC):
    @abstractmethod
    def save(self, run: Run) -> None:
        """Persist a run entity."""
        pass

    @abstractmethod
    def get(self, run_id: str) -> Optional[Run]:
        """Retrieve a run entity by its ID."""
        pass

    @abstractmethod
    def list_by_experiment(self, experiment_id: str) -> list[Run]:
        """List all runs for a specific experiment."""
        pass
