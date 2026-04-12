# Doshi-Velez Lab Knowledge Base

## Core Research Pillars

### 1. Clinical RL Safety (Deadly Triad, OPE)
Focuses on the challenges of applying Reinforcement Learning in clinical settings. Key issues include the "Deadly Triad" (function approximation, bootstrapping, and off-policy learning) and the development of robust Off-Policy Evaluation (OPE) methods to safely estimate the value of new policies using historical data.

### 2. Human-AI Interaction (Automation Bias, XAI)
Investigates how clinicians interact with AI recommendations. This includes studying "Automation Bias" (the tendency to over-rely on automated systems) and developing eXplainable AI (XAI) techniques that provide meaningful insights to improve clinical decision-making rather than just providing a black-box recommendation.

### 3. Causal Inference in EHR
Leverages Electronic Health Record (EHR) data to perform causal inference. This involves developing methods to handle the complexities of observational data, such as confounding and selection bias, to identify treatment effects and inform personalized medicine.

### 4. The Myth of Generalizability
Challenges the assumption that AI models trained in one clinical environment will automatically perform well in another. This pillar emphasizes that models often learn local clinical practices and administrative patterns rather than underlying biological truths, making local validation more critical than global performance metrics like AUROC.

### 5. Continuous-Time Risk Modeling (Neural SDEs)
Utilizes Neural Stochastic Differential Equations (Neural SDEs) to model clinical risk trajectories in continuous time. This approach is particularly effective for high-frequency data (e.g., EMA) and allows for forecasting risk at any temporal point, constrained by clinical interpretability (e.g., compact state spaces).

### 6. mHealth and Real-Time RL Monitoring
Focuses on the deployment of Reinforcement Learning in mobile health settings. This includes developing "algorithm fidelity" frameworks to monitor autonomous agents in real-time, ensuring participant safety and ensuring that the AI behavior aligns with trial protocols.

### 7. Algorithm Aversion & Human-Labeling Bias
Investigates the psychological and systemic barriers to AI adoption. Research shows a "human-labeling bias" where clinicians are more likely to trust recommendations attributed to human peers than to AI, highlighting the need for better human-AI alignment and trust-building strategies.
