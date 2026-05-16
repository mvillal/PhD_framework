from datetime import datetime
from src.domain.experiment.entities import RunStatus
from tests.mothers.entity_mother import RunMother, MetricMother


def test_run_initialization():
    run = RunMother.create(experiment_id="test-exp", run_name="test-run")
    assert run.experiment_id == "test-exp"
    assert run.name == "test-run"
    assert run.status == RunStatus.PENDING
    assert len(run.metrics) == 0
    assert len(run.steps) == 0


def test_run_transitions():
    run = RunMother.create()

    run.start()
    assert run.status == RunStatus.RUNNING
    assert isinstance(run.start_time, datetime)

    run.complete()
    assert run.status == RunStatus.COMPLETED
    assert isinstance(run.end_time, datetime)


def test_add_step():
    run = RunMother.create()
    run.add_step("test-step", "test-explanation", metadata={"key": "val"})

    assert len(run.steps) == 1
    assert run.steps[0].name == "test-step"
    assert run.steps[0].explanation == "test-explanation"
    assert run.steps[0].metadata == {"key": "val"}


def test_metric_creation():
    metric = MetricMother.create(key="loss", value=0.5, step=1)
    assert metric.key == "loss"
    assert metric.value == 0.5
    assert metric.step == 1
