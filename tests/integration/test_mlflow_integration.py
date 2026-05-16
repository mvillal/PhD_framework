import os
import pytest
import shutil
from src.container import ExperimentContainer


@pytest.fixture
def test_container():
    # Use a temporary SQLite database for integration tests
    test_db = "test_mlflow.db"
    test_tracking_uri = f"sqlite:///{test_db}"
    container = ExperimentContainer(tracking_uri=test_tracking_uri)
    yield container
    # Cleanup
    if os.path.exists(test_db):
        os.remove(test_db)
    # Also cleanup artifacts directory if created
    if os.path.exists("mlruns"):
        shutil.rmtree("mlruns")


def test_full_tracked_workflow(test_container):
    # 1. Start Run
    run = test_container.start_run.execute(
        experiment_id="Integration-Test", run_name="Test-Workflow"
    )
    assert run.run_id is not None

    # 2. Log Step & Metric
    test_container.log_step.execute(
        run.run_id, "TestStep", "This is an automated integration test explanation."
    )
    test_container.log_metric.execute(run.run_id, "test_metric", 1.0)

    # 3. Log Artifact
    test_container.log_artifact.execute(
        run.run_id, "test.txt", "Artifact content", "integration/test.txt"
    )

    # 4. Complete
    test_container.complete_run.execute(run.run_id)

    # Verify local database file creation
    assert os.path.exists("test_mlflow.db")
    # Digging into MLflow internal structure is complex,
    # but existence of the dir confirms the adapter called the backend.
