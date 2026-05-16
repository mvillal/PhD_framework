import time
import random
from src.container import container


def train_dummy_model():
    # 1. Start a new run
    print("🚀 Starting Experiment Run...")
    run = container.start_run.execute(
        experiment_id="Psychiatric-Risk-Forecasting", run_name="Neural-SDE-Baseline"
    )

    try:
        # 2. Simulate training loops
        epochs = 5
        for epoch in range(epochs):
            print(f"--- Epoch {epoch} ---")

            # Simulate metrics
            loss = 0.5 / (epoch + 1) + random.uniform(0, 0.1)
            accuracy = 0.8 + (epoch * 0.03) + random.uniform(-0.01, 0.01)

            # Log metrics via use case
            container.log_metric.execute(run.run_id, "loss", loss, step=epoch)
            container.log_metric.execute(run.run_id, "accuracy", accuracy, step=epoch)

            print(f"Logged Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")
            time.sleep(1)

        # 3. Complete the run
        print("✅ Training Complete. Finalizing run...")
        container.complete_run.execute(run.run_id)

    except Exception as e:
        print(f"❌ Run failed: {e}")
        # In a full implementation, we'd have a FailRunUseCase


if __name__ == "__main__":
    train_dummy_model()
