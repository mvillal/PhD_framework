from typing import Dict, List, Optional
from src.domain.experiment.entities import Run
from src.application.ports.interfaces import RunRepositoryPort

class InMemoryRunRepository(RunRepositoryPort):
    def __init__(self):
        self._runs: Dict[str, Run] = {}

    def save(self, run: Run) -> None:
        self._runs[run.run_id] = run

    def get(self, run_id: str) -> Optional[Run]:
        return self._runs.get(run_id)

    def list_by_experiment(self, experiment_id: str) -> List[Run]:
        return [run for run in self._runs.values() if run.experiment_id == experiment_id]
