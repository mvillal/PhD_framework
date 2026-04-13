# Med-Gemini

## 📄 Definition
**Med-Gemini** is a family of natively multimodal clinical foundation models developed by Google DeepMind (2024). It is designed to process and reason across text, medical imaging (radiology, pathology), long-form patient histories, and clinical signals (ECG/EEG).

## 🛠️ Key Technologies
- **Uncertainty-Guided Search (UGS):** A core innovation where the model assesses its own confidence. If internal knowledge is insufficient for a complex case, it autonomously triggers external clinical database queries or web searches to ground its reasoning.
- **Long-Context Reasoning:** Capable of processing up to millions of tokens, enabling the synthesis of a patient's entire longitudinal record in a single reasoning step.
- **Natively Multimodal Architecture:** Built from the ground up to understand visual pathologies and textual clinical notes without separate specialized encoders for each modality.

## 🩺 Clinical Relevance
Med-Gemini represents a shift toward "grounded" AI that acknowledges its own uncertainty, significantly reducing the risk of medical hallucination in high-stakes diagnostic settings.

## 🔗 Related Entities
- [[deepmind_clinical_ai]]
- [[agentic_ai]]
