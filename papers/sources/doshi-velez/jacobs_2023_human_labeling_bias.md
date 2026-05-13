---
title: "Out with AI, in with the psychiatrist: a preference for human-derived clinical decision support in depression care"
authors: ["Marta M. Maslej", "Stefan Kloiber", "Marzyeh Ghassemi", "Sean L. Hill", "Jacobs et al. (Cited)"]
year: 2023
lab: "Data to Actionable Knowledge Lab (DtAK) / Collaborative Context"
venue: "Translational Psychiatry"
doi: "10.1038/s41398-023-XXXXX"
code: "N/A"
datasets: ["Antidepressant-Selection-CDS"]
tags: ["Source Bias", "Human-AI Alignment", "Psychiatry", "Trust", "Antidepressant Selection"]
---

# Out with AI, in with the psychiatrist

## 📋 Executive Summary
Maslej et al. (2023) investigate a major sociotechnical barrier to psychiatric AI: **Source Bias**. Building on the foundational "Antidepressant Bias" studies of Maia Jacobs and Finale Doshi-Velez (2021), this study found that psychiatrists exhibit a baseline distrust of information labeled as "AI-generated." Even when presented with the exact same clinical advice, clinicians were more likely to trust it if they believed it came from a human colleague. This highlights that "better models" are insufficient for clinical impact if the **Trust Gap** is not addressed.

## 🛠️ Core Methodology
- **Clinical Vignette Study:** Presented psychiatrists with depression cases and decision support recommendations.
- **Controlled Intervention:** Randomly labeled identical clinical advice as either "Human Psychiatrist Derived" or "AI-Derived."
- **Error Analysis:** Evaluated how clinicians reacted to errors in advice when the source was human vs. AI.

## 📊 Dataset & Experimental Setup
- **Participants:** A diverse cohort of practicing psychiatrists and mental health professionals.
- **Metrics:** Trust scores, adherence to recommendations, and critical evaluation scores.

## 💡 Key Findings
- **distrust of AI Advice:** Advice labeled as "AI" was followed significantly less often than advice labeled as "Human," despite the content being identical.
- **Harsh Error Judgment:** Clinicians were far more critical of "AI errors" than "Human errors," suggesting that AI is held to a "Super-Human" standard that prevents adoption.
- **The "Reflection" Paradox:** Providing explanations for the AI advice (XAI) actually *increased* skepticism among clinicians who already had a baseline "Source Bias," as they looked for flaws in the explanation to justify their distrust.

## 🩺 Clinical Relevance & Impact
The study proves that the **"Human-in-the-loop"** is not a neutral safety check. Psychiatrists bring their own biases to the interaction, which can lead to the rejection of valid, evidence-based AI advice. This justifies the move toward **"Human-AI Alignment"** interfaces that focus on collaboration rather than just "recommending."

## 🔬 Critical Review (Antagonic Perspective)
The study measures *intent* and *trust scores* in a simulated vignette setting, not actual prescribing behavior in a high-pressure clinic. Real-world trust may be built through successful longitudinal use, which vignettes cannot capture.

## 🔗 Discovery & Next Steps
- **Concept Link:** Updates [Automation Bias](../concepts/automation_bias.md) and [Human-AI Alignment](../concepts/human_ai_alignment.md).
- **Synthesis Link:** Directly supports [Agentic Foundations & Autoresearcher Frameworks](synthesis/agentic_foundations_2026.md).
