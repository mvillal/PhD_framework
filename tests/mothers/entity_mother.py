from datetime import datetime
from uuid import uuid4
from src.domain.experiment.entities import Run, Metric, Step, Artifact, RunStatus

class RunMother:
    @staticmethod
    def create(
        experiment_id: str = "default-exp",
        run_name: str = "default-run",
        status: RunStatus = RunStatus.PENDING
    ) -> Run:
        return Run(
            experiment_id=experiment_id,
            run_id=str(uuid4()),
            name=run_name,
            status=status
        )

    @staticmethod
    def completed_run(experiment_id: str = "default-exp") -> Run:
        run = RunMother.create(experiment_id=experiment_id, status=RunStatus.COMPLETED)
        run.start_time = datetime.now()
        run.end_time = datetime.now()
        return run

class MetricMother:
    @staticmethod
    def create(key: str = "loss", value: float = 0.5, step: int = 0) -> Metric:
        return Metric(key=key, value=value, step=step)

class StepMother:
    @staticmethod
    def create(name: str = "Research", explanation: str = "Default explanation") -> Step:
        return Step(name=name, explanation=explanation)

class ArtifactMother:
    @staticmethod
    def create(name: str = "summary.md", content: str = "# Summary") -> Artifact:
        return Artifact(name=name, content=content, path=f"output/{name}")
