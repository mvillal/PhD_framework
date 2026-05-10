import pytest
from src.application.use_cases.tracker_use_cases import StartRunUseCase, LogMetricUseCase
from src.application.ports.interfaces import ExperimentTrackerPort, RunRepositoryPort
from src.domain.experiment.entities import Run
from tests.mothers.entity_mother import RunMother

def test_start_run_use_case(mocker):
    # Mock ports
    mock_tracker = mocker.Mock(spec=ExperimentTrackerPort)
    mock_repo = mocker.Mock(spec=RunRepositoryPort)
    
    use_case = StartRunUseCase(mock_tracker, mock_repo)
    run = use_case.execute(experiment_id="test-exp", run_name="test-run")
    
    assert isinstance(run, Run)
    assert run.name == "test-run"
    mock_repo.save.assert_called_once()
    # We ignore the exact run object since ID is random
    mock_tracker.start_run.assert_called_once()

def test_log_metric_use_case(mocker):
    mock_tracker = mocker.Mock(spec=ExperimentTrackerPort)
    mock_repo = mocker.Mock(spec=RunRepositoryPort)
    
    # Setup repo mock with Mother
    run = RunMother.create()
    mock_repo.get.return_value = run
    
    use_case = LogMetricUseCase(mock_tracker, mock_repo)
    use_case.execute(run_id=run.run_id, key="accuracy", value=0.9, step=1)
    
    assert len(run.metrics) == 1
    assert run.metrics[0].key == "accuracy"
    mock_repo.save.assert_called_once()
    mock_tracker.log_metric.assert_called_once()
