---
title: "LLM OS & Agentic Engineering (Karpathy Paradigms)"
authors: ["Andrej Karpathy"]
year: 2024-2026
tags: ["LLM OS", "Agentic Engineering", "RLVR", "System 2 Thinking", "Eureka Labs"]
---

# LLM OS & Agentic Engineering

## 📋 Overview
Developed by Andrej Karpathy (OpenAI, Tesla, Eureka Labs), these concepts redefine the LLM from a "chatbot" to the **central processing unit (CPU)** of a new computing stack.

**Source:** [Karpathy 2024](../../sources/autoresearchers/karpathy_2024_llm_os.md)

## 🛠️ Core Concepts

### 1. The LLM OS
The LLM acts as the kernel of an operating system, managing resources and executing "system calls":
*   **CPU = LLM Kernel:** Interprets instructions and orchestrates tasks.
*   **RAM = Context Window:** Active working memory for immediate reasoning.
*   **File System = RAG/Search:** Long-term storage and retrieval of structured data (Markdown/Wikis).
*   **Peripherals = Tools/APIs:** Calculators, Python interpreters, and web browsers.

### 2. RLVR (Reinforcement Learning with Verifiable Rewards)
The "engine" of 2025/2026 models. Instead of relying solely on human preference (RLHF), models are trained in environments where truth is **verifiable** (e.g., Code, Math, Clinical Guidelines). 
*   **Reasoning Traces:** Models learn to "think out loud" (System 2) and verify their own intermediate steps.
*   **Self-Correction:** The agent detects errors in its own logic or code before outputting a final answer.

### 3. Agentic Engineering (The AutoResearch Pattern)
A workflow for autonomous research and development:
*   **Programmatic Specs:** Agents are given a `program.md` specification.
*   **Infinite Loops:** Agents run overnight, executing code, evaluating failures, and optimizing their own prompts until the objective is met.
*   **Vibe Coding:** High-level delegation where the researcher "vibes" the architecture while the agentic stack handles the implementation and testing.

## 🩺 Clinical Application in Psychiatry
In the PhD Framework, the LLM OS paradigm is used to:
1.  **Orchestrate Multi-Lab Research:** The Wiki acts as the "File System," while agents act as specialized "Processes."
2.  **Verifiable Clinical Reasoning:** Using RLVR logic to ensure that clinical risk forecasts (e.g., suicide risk) are grounded in verifiable patient history rather than "hallucinated vibes."

## 🔗 Related Concepts
- [Agentic AI](agentic_ai.md)
- [Med-Gemini](med_gemini.md)
- [Causal Falsification](causal_falsification.md) (as a form of verifiable reward)

---
**Source Grounding:** Based on Andrej Karpathy's 2024-2026 public discourse, Eureka Labs mission, and the "LLM OS" talk.
