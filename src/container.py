from src.infrastructure.repositories.in_memory_repo import InMemoryRunRepository
from src.infrastructure.adapters.mlflow_tracker import MLflowTrackerAdapter
from src.application.use_cases.tracker_use_cases import (
    StartRunUseCase, 
    LogMetricUseCase, 
    CompleteRunUseCase,
    LogAgentStepUseCase,
    LogArtifactUseCase
)

class ExperimentContainer:
    """
    A simple Dependency Injection container to bootstrap the tracking framework.
    """
    def __init__(self, tracking_uri: str = "sqlite:///mlflow.db"):
        # Infrastructure
        self.repository = InMemoryRunRepository()
        # Using SQLite by default for 2026 stability
        self.tracker = MLflowTrackerAdapter(tracking_uri=tracking_uri)

        # Application Use Cases
        self.start_run = StartRunUseCase(self.tracker, self.repository)
        self.log_metric = LogMetricUseCase(self.tracker, self.repository)
        self.log_step = LogAgentStepUseCase(self.tracker, self.repository)
        self.log_artifact = LogArtifactUseCase(self.tracker, self.repository)
        self.complete_run = CompleteRunUseCase(self.tracker, self.repository)

# Global container instance
container = ExperimentContainer()
