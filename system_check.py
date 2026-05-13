import sys
import torch
import numpy as np
import pandas as pd
import mlflow
from pathlib import Path

def run_health_checks():
    print("🔬 --- PhD Framework System Health Check ---")
    
    # 1. Environment Verification
    print(f"\n[Environment]")
    print(f"Python Version: {sys.version}")
    print(f"Project Root: {Path(__file__).parent}")
    
    # 2. Dependency Verification
    print(f"\n[Dependencies]")
    print(f"PyTorch Version: {torch.__version__}")
    print(f"NumPy Version: {np.__version__}")
    print(f"Pandas Version: {pd.__version__}")
    print(f"MLflow Version: {mlflow.__version__}")
    
    # 3. Hardware Acceleration (Critical for Models)
    print(f"\n[Hardware Acceleration]")
    if torch.cuda.is_available():
        print(f"✅ CUDA is available (NVIDIA GPU detected)")
        print(f"Device Name: {torch.cuda.get_device_name(0)}")
        print(f"CUDA Version: {torch.version.cuda}")
    elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        print(f"✅ MPS is available (Apple Silicon detected)")
    else:
        print(f"⚠️ GPU acceleration not detected. Future modeling will run on CPU.")

    # 4. Tracking Backend Verification
    print(f"\n[Experiment Tracking]")
    try:
        from src.container import container
        print(f"✅ Tracking Container Initialized.")
        print(f"Default Tracking URI: {mlflow.get_tracking_uri()}")
    except Exception as e:
        print(f"❌ Tracking Initialization Failed: {e}")

    # 5. Wiki Integrity (Quick Scan)
    print(f"\n[Wiki Integrity]")
    sources_count = len(list(Path("papers/sources").rglob("*.md")))
    wiki_count = len(list(Path("papers/wiki").rglob("*.md")))
    print(f"Source Files Found: {sources_count}")
    print(f"Wiki Pages Found: {wiki_count}")
    
    print("\n✅ Health Check Complete. Ready for Implementation phase.")

if __name__ == "__main__":
    run_health_checks()
