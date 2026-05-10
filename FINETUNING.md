# Model Fine-Tuning Strategy

This document outlines the strategy for extending the PhD Framework to support a wide spectrum of fine-tuning techniques, from parameter-efficient modern methods to classical architectural-agnostic paradigms.

## 🎯 Fine-Tuning Taxonomy

We categorize fine-tuning into three primary pillars based on plasticity and resource requirements.

### 1. Parameter-Efficient Fine-Tuning (PEFT/LoRA)
Focuses on updating <1% of parameters to prevent catastrophic forgetting and enable training on consumer hardware.
- **Best For:** Low-data regimes, multi-task adapter swapping, on-premise clinical deployment.
- **Pattern:** [See QLoRA Implementation below](#-implementation-pattern-qlora).

### 2. Classical Full Fine-Tuning (FFT)
Updates all model weights via backpropagation.
- **Best For:** High-data regimes where maximum performance is the ceiling and computational resources (H100/A100) are abundant.
- **Technique: Selective Freezing:** A hybrid approach where the "backbone" is frozen initially, and only the "head" or specific layers (e.g., late-stage transformers) are updated.

### 3. Architecture-Agnostic Techniques
Methods that can be applied regardless of the underlying model structure (CNN, ViT, LLM).
- **Knowledge Distillation (KD):** Training a "Student" model to mimic the output distribution (logits) of a larger "Teacher" model. Critical for deploying high-fidelity clinical models to edge devices.
- **Domain Adaptation (DA):** Aligning the feature distributions between a source domain (e.g., public Biobank data) and a target clinical domain (e.g., local hospital EHR) using techniques like **CORAL** or **DANN**.
- **Data-Centric Fine-Tuning:** Improving performance not by changing the architecture, but by identifying and fixing "Measurement Gaps" or human labeling noise (Jacobs et al. 2023) using tools like `cleanlab`.

---

## 🛠️ Implementation Patterns

### A. Classical Layer Freezing (PyTorch)
Useful for stabilizing training in small psychiatric datasets.

```python
import torch.nn as nn

def setup_classical_finetune(model: nn.Module):
    # 1. Freeze entire backbone
    for param in model.parameters():
        param.requires_grad = False
    
    # 2. Unfreeze specific target layers (e.g., last 2 blocks)
    for param in model.transformer.layers[-2:].parameters():
        param.requires_grad = True
        
    # 3. Use Discriminative Learning Rates
    optimizer = torch.optim.Adam([
        {'params': model.head.parameters(), 'lr': 1e-3},
        {'params': model.transformer.layers[-2:].parameters(), 'lr': 1e-4}
    ])
    return model, optimizer
```

### B. Knowledge Distillation
Architecture-agnostic method to compress heavy clinical foundations (AMIE/Med-Gemini) into research-ready student models.

```python
import torch.nn.functional as F

def distillation_loss(student_logits, teacher_logits, labels, T=2.0, alpha=0.5):
    # Standard Cross Entropy
    hard_loss = F.cross_entropy(student_logits, labels)
    
    # "Soft" Distillation Loss (KL Divergence)
    soft_loss = F.kl_div(
        F.log_softmax(student_logits / T, dim=1),
        F.softmax(teacher_logits / T, dim=1),
        reduction='batchmean'
    ) * (T * T)
    
    return alpha * hard_loss + (1 - alpha) * soft_loss
```

### C. QLoRA (Parameter-Efficient)
[... existing implementation pattern ...]

## 🚀 Future Extensions
1.  **RLHF / DPO:** Extending fine-tuning to include Direct Preference Optimization for human-AI alignment in clinical dialogue.
2.  **Multimodal Fine-Tuning:** Adapting RETFound models for specific uveitis lesion segmentation using the same PEFT patterns.
3.  **Distributed Training:** Utilizing the **Ray RLlib** patterns identified in our research to scale fine-tuning across multiple GPUs in GKE.
