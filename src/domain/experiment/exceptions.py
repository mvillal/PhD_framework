class DomainError(Exception):
    """Base class for all domain exceptions."""

    pass


class RunError(DomainError):
    """Base class for all run-related exceptions."""

    pass


class RunNotFoundError(RunError):
    """Raised when a requested run is not found."""

    def __init__(self, run_id: str):
        self.run_id = run_id
        super().__init__(f"Run with ID '{run_id}' was not found.")


class RunStateError(RunError):
    """Raised when an operation is invalid for the current run state."""

    pass


class ExperimentError(DomainError):
    """Base class for all experiment-related exceptions."""

    pass


class ExperimentNotFoundError(ExperimentError):
    """Raised when a requested experiment is not found."""

    def __init__(self, experiment_id: str):
        self.experiment_id = experiment_id
        super().__init__(f"Experiment with ID '{experiment_id}' was not found.")
