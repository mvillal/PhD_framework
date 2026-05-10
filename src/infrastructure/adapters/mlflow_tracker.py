import mlflow
from datetime import datetime
from src.domain.experiment.entities import Run, Metric, Parameter, Step, Artifact
from src.application.ports.interfaces import ExperimentTrackerPort

class MLflowTrackerAdapter(ExperimentTrackerPort):
    def __init__(self, tracking_uri: str = "http://localhost:5000"):
        mlflow.set_tracking_uri(tracking_uri)

    def start_run(self, run: Run) -> None:
        mlflow.set_experiment(run.experiment_id)
        # We start the mlflow run. 
        # Note: We don't use mlflow's automatic run_id generation for our entity run_id 
        # to keep domain pure, but we can tag it.
        active_run = mlflow.start_run(run_name=run.name)
        mlflow.set_tag("domain_run_id", run.run_id)

    def log_metric(self, run_id: str, metric: Metric) -> None:
        # In a real async scenario, we'd need to ensure we are in the correct context
        mlflow.log_metric(metric.key, metric.value, step=metric.step)

    def log_parameter(self, run_id: str, parameter: Parameter) -> None:
        mlflow.log_param(parameter.key, parameter.value)

    def log_step(self, run_id: str, step: Step) -> None:
        # We log the explanation as an artifact (text file)
        filename = f"steps/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{step.name}.txt"
        mlflow.log_text(step.explanation, filename)
        # Also log metadata as tags if small
        for k, v in step.metadata.items():
            mlflow.set_tag(f"step_{step.name}_{k}", v)

    def log_artifact(self, run_id: str, artifact: Artifact) -> None:
        mlflow.log_text(artifact.content, artifact.path)

    def end_run(self, run_id: str, status: str) -> None:
        # Status mapping could be more sophisticated
        mlflow_status = "FINISHED" if status == "COMPLETED" else "FAILED"
        mlflow.end_run(status=mlflow_status)
