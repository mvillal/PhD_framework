from src.domain.experiment.entities import Run, Metric, Parameter, RunStatus
from src.application.ports.interfaces import ExperimentTrackerPort, RunRepositoryPort

class StartRunUseCase:
    def __init__(self, tracker: ExperimentTrackerPort, repository: RunRepositoryPort):
        self.tracker = tracker
        self.repository = repository

    def execute(self, experiment_id: str, run_name: str = None) -> Run:
        run = Run(experiment_id=experiment_id, name=run_name)
        run.start()
        self.repository.save(run)
        self.tracker.start_run(run)
        return run

class LogMetricUseCase:
    def __init__(self, tracker: ExperimentTrackerPort, repository: RunRepositoryPort):
        self.tracker = tracker
        self.repository = repository

    def execute(self, run_id: str, key: str, value: float, step: int = None) -> None:
        run = self.repository.get(run_id)
        if not run:
            raise ValueError(f"Run {run_id} not found")
        
        metric = Metric(key=key, value=value, step=step)
        run.metrics.append(metric)
        self.repository.save(run)
        self.tracker.log_metric(run_id, metric)

class LogAgentStepUseCase:
    def __init__(self, tracker: ExperimentTrackerPort, repository: RunRepositoryPort):
        self.tracker = tracker
        self.repository = repository

    def execute(self, run_id: str, step_name: str, explanation: str, metadata: dict = None) -> None:
        run = self.repository.get(run_id)
        if not run:
            raise ValueError(f"Run {run_id} not found")
        
        step = run.add_step(name=step_name, explanation=explanation, metadata=metadata)
        self.repository.save(run)
        self.tracker.log_step(run_id, step)

class LogArtifactUseCase:
    def __init__(self, tracker: ExperimentTrackerPort, repository: RunRepositoryPort):
        self.tracker = tracker
        self.repository = repository

    def execute(self, run_id: str, name: str, content: str, path: str) -> None:
        run = self.repository.get(run_id)
        if not run:
            raise ValueError(f"Run {run_id} not found")
        
        artifact = run.add_artifact(name=name, content=content, path=path)
        self.repository.save(run)
        self.tracker.log_artifact(run_id, artifact)

class CompleteRunUseCase:
    def __init__(self, tracker: ExperimentTrackerPort, repository: RunRepositoryPort):
        self.tracker = tracker
        self.repository = repository

    def execute(self, run_id: str) -> None:
        run = self.repository.get(run_id)
        if not run:
            raise ValueError(f"Run {run_id} not found")
        
        run.complete()
        self.repository.save(run)
        self.tracker.end_run(run_id, status="COMPLETED")
