from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class RunStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class Metric:
    key: str
    value: float
    timestamp: datetime = field(default_factory=datetime.now)
    step: int | None = None


@dataclass(frozen=True)
class Parameter:
    key: str
    value: str


@dataclass(frozen=True)
class Step:
    name: str
    explanation: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Artifact:
    name: str
    content: str
    path: str


@dataclass
class Run:
    experiment_id: str
    run_id: str = field(default_factory=lambda: str(uuid4()))
    name: str | None = None
    status: RunStatus = RunStatus.PENDING
    start_time: datetime | None = None
    end_time: datetime | None = None
    parameters: dict[str, str] = field(default_factory=dict)
    metrics: list[Metric] = field(default_factory=list)
    steps: list[Step] = field(default_factory=list)
    artifacts: list[Artifact] = field(default_factory=list)

    def start(self) -> None:
        self.status = RunStatus.RUNNING
        self.start_time = datetime.now()

    def complete(self) -> None:
        self.status = RunStatus.COMPLETED
        self.end_time = datetime.now()

    def fail(self) -> None:
        self.status = RunStatus.FAILED
        self.end_time = datetime.now()

    def add_step(
        self, name: str, explanation: str, metadata: dict[str, str] | None = None
    ) -> Step:
        step = Step(name=name, explanation=explanation, metadata=metadata or {})
        self.steps.append(step)
        return step

    def add_artifact(self, name: str, content: str, path: str) -> Artifact:
        artifact = Artifact(name=name, content=content, path=path)
        self.artifacts.append(artifact)
        return artifact

    def add_metric(self, key: str, value: float, step: int | None = None) -> Metric:
        metric = Metric(key=key, value=value, step=step)
        self.metrics.append(metric)
        return metric

    def add_parameter(self, key: str, value: str) -> Parameter:
        parameter = Parameter(key=key, value=value)
        self.parameters[key] = value
        return parameter


@dataclass(frozen=True)
class Experiment:
    id: str
    name: str
    description: str | None = None
    created_at: datetime = field(default_factory=datetime.now)
