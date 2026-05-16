from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
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
    step: Optional[int] = None


@dataclass(frozen=True)
class Parameter:
    key: str
    value: str


@dataclass(frozen=True)
class Step:
    name: str
    explanation: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Artifact:
    name: str
    content: str
    path: str


@dataclass
class Run:
    experiment_id: str
    run_id: str = field(default_factory=lambda: str(uuid4()))
    name: Optional[str] = None
    status: RunStatus = RunStatus.PENDING
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    parameters: Dict[str, str] = field(default_factory=dict)
    metrics: List[Metric] = field(default_factory=list)
    steps: List[Step] = field(default_factory=list)
    artifacts: List[Artifact] = field(default_factory=list)

    def start(self):
        self.status = RunStatus.RUNNING
        self.start_time = datetime.now()

    def complete(self):
        self.status = RunStatus.COMPLETED
        self.end_time = datetime.now()

    def fail(self):
        self.status = RunStatus.FAILED
        self.end_time = datetime.now()

    def add_step(self, name: str, explanation: str, metadata: Dict[str, str] = None):
        step = Step(name=name, explanation=explanation, metadata=metadata or {})
        self.steps.append(step)
        return step

    def add_artifact(self, name: str, content: str, path: str):
        artifact = Artifact(name=name, content=content, path=path)
        self.artifacts.append(artifact)
        return artifact


@dataclass(frozen=True)
class Experiment:
    id: str
    name: str
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
