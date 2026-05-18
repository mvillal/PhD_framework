# Title: Dynamic Fidelity-Constrained Reinforcement Learning for Psychiatric Digital Interventions

## Abstract / Executive Summary
This proposal introduces a novel framework for resolving the inherent tension between algorithmic adaptivity and statistical utility in live clinical trials of psychiatric digital interventions (e.g., mHealth, Ecological Momentary Assessments). Highly adaptive Reinforcement Learning (RL) agents often "game" clinical environments by converging on niche states that maximize proximal rewards but degrade the trial's Off-Policy Evaluation (OPE) capabilities and violate protocol fidelity. Drawing on principles of safe clinical RL and algorithm fidelity monitoring, we propose a Dynamic Fidelity-Constrained RL architecture. This system employs real-time estimation of statistical power (via Effective Sample Size) and patient volatility to dynamically modulate the agent's exploration boundaries. During euthymic (stable) periods, exploration bounds expand to capture high-variance causal data. Conversely, during periods of psychiatric instability or high informative missingness, the policy strictly tightens to conservative, high-fidelity safety protocols. This approach ensures both participant safety and the preservation of rigorous scientific utility.

## Background & Motivation (The Adaptivity vs. Fidelity Conflict)
The deployment of sequential decision-making algorithms in healthcare requires navigating the critical tradeoff between optimizing patient outcomes and preserving the ability to rigorously evaluate the intervention. As highlighted by Gottesman et al. (2019), "evaluation is harder than optimization," and offline success does not guarantee prospective safety. In live trials, such as those monitored for Algorithm Fidelity (Trella et al., 2024), RL agents present a unique "Adaptivity Trap." Driven to maximize cumulative rewards, agents may over-exploit specific intervention types or temporal niches, effectively eliminating the stochasticity required to compute reliable causal estimators. This lack of exploration prevents the subsequent statistical comparison of treatments, violating the fundamental scientific utility of the trial.

Furthermore, in psychiatric contexts, patient states are highly non-stationary and partially observable. Informative missingness—where the absence of an Ecological Momentary Assessment (EMA) response is a strong indicator of clinical state—further complicates reward optimization. Static safety boundaries, while providing baseline safeguarding, fail to capitalize on periods of patient stability where valuable counterfactual data could be safely gathered. A static approach forces a compromise: either constrain the agent so much that it fails to personalize, or allow adaptivity at the cost of trial fidelity and patient safety during crises.

## Proposed Architecture (Dynamic Fidelity-Constrained RL)

The proposed architecture introduces a dual-objective RL framework that explicitly balances expected reward with a dynamic constraint on algorithm fidelity and statistical power.

### State Representation (Including Informative Missingness & Volatility)
The patient state $S_t$ is modeled as a Partially Observable Markov Decision Process (POMDP). Crucially, the state space explicitly encodes both longitudinal clinical markers and meta-features of the interaction:
- **Clinical Volatility Index:** A real-time latent variable estimating the variance in the patient's mood or symptom trajectory.
- **Informative Missingness:** Explicit encoding of non-response patterns (e.g., time since last EMA, consecutive missed prompts) as indicative state features, acknowledging that missing data in psychiatry is often a proxy for severe depressive or manic episodes.

### Dynamic Fidelity Controller (Real-time Statistical Power Estimation)
To preserve the scientific utility of the trial, a secondary controller continuously monitors the policy's behavior against the trial's target distribution.
- **Effective Sample Size (ESS) Monitoring:** The controller computes the real-time ESS using Importance Sampling weights comparing the current RL behavioral policy to a uniform/baseline exploration policy.
- **Fidelity Boundaries:** When ESS drops below a critical threshold (indicating the agent is "gaming" a niche state and destroying counterfactual overlap), the controller generates a penalty signal to force diversification of actions.

### Constrained Policy Optimization
The RL agent operates under a dynamically bounded action space.
- **Euthymic Expansion:** When the Volatility Index is low and ESS is healthy, the exploration boundaries expand. The agent is permitted to test a wider array of intervention timings and contents to gather high-variance causal data.
- **Crisis Contraction:** If the Volatility Index spikes, or informative missingness indicates a potential crisis, the action space strictly collapses to a pre-defined, conservative "high-fidelity" safety protocol. This ensures participant safeguarding (Trella et al., 2024) and aligns with clinically reasonable bounds (Gottesman et al., 2019).

## Methodological Framework

To mathematically formalize and rigorously validate the architecture, the following statistical methods are employed:

### 1. Modeling Volatility and Informative Missingness
Standard discrete-time POMDPs fail when confronted with highly irregular EMA sampling.
*   **Clinical Volatility Index via Compact Neural SDEs:** We model the patient’s latent psychiatric state $X_t$ using a Neural Stochastic Differential Equation (Neural SDE). The formulation is $dX_t = f_\theta(X_t, t)dt + g_\phi(X_t, t)dW_t$. The diffusion term $g_\phi(\cdot)$ directly serves as the real-time "Clinical Volatility Index." To prevent divergence in sparse data regimes, a compact state space (e.g., a diffeomorphic mapping to $[0,1]$) is enforced.
*   **Informative Missingness (MNAR) as a Hawkes-Modulated Observation Process:** Missing EMA prompts are an active clinical signal. We model observation timestamps using a state-dependent Hawkes Process. The baseline intensity $\lambda_0(t)$ is inversely coupled to the latent state severity $X_t$ and the diffusion $g_\phi(X_t, t)$, mathematically encoding the "Silent Smoke Detector" effect.

### 2. Real-Time ESS & The Dynamic Fidelity Controller
*   **Marginalized Importance Sampling (MIS):** Instead of trajectory-level ratios, the Dynamic Fidelity Controller estimates the stationary state-action density ratio $w(s,a) = \frac{d^{\pi_e}(s,a)}{d^{\pi_b}(s,a)}$ using Minimax Weight Learning, breaking the variance explosion in long-horizon EMA trials.
*   **Sequential ESS Formulation:** The real-time proxy for statistical power is computed via the generalized Kish’s Effective Sample Size applied to the MIS weights: $ESS_t = \frac{(\sum_{i=1}^n w(s_i, a_i))^2}{\sum_{i=1}^n w(s_i, a_i)^2}$.
*   **Fidelity Contraction via KL-Penalty:** When $ESS_t < \tau_{crit}$, the controller dynamically scales a penalty term $\lambda_t D_{KL}(\pi_\theta(\cdot|s_t) || \pi_{safe}(\cdot|s_t))$, forcing contraction back to an expert-defined baseline protocol.

### 3. Off-Policy Evaluation (OPE)
*   **Marginalized Doubly Robust (MDR) Estimator:** We evaluate the policy combining a Q-function (outcome model) with the MIS density ratios (treatment model), providing a low-variance, unbiased bound.
*   **Causal Falsification Check:** Before accepting OPE bounds, a falsification test using a Structural Causal Model (SCM) with negative control variables (e.g., exogenous weather) checks for unmeasured confounding.

### 4. Synthetic EMA Generation (Simulation)
*   **Latent Similarity Gaussian Processes (LSGP) + SDE-GANs:** Synthetic cohorts are generated by mapping real trajectories to a latent space using LSGPs, then training a Continuous-Time Generative Adversarial Network (SDE-GAN) on this space.
*   **Bayesian Non-parametric Stress Testing:** We "red-team" the RL agent by injecting anomalous state transitions using a Hierarchical Dirichlet Process Hidden Markov Model (HDP-HMM) overlaid on the SDE, simulating sudden shifts into "crisis states" to test the rapid contraction capabilities of the Fidelity Controller.

## Key Hypotheses
1. **Hypothesis 1 (Scientific Utility):** The Dynamic Fidelity-Constrained RL agent will maintain a significantly higher Effective Sample Size (ESS) for Off-Policy Evaluation at the trial's conclusion compared to an unconstrained, reward-maximizing agent.
2. **Hypothesis 2 (Safety and Safeguarding):** The dynamic contraction of exploration bounds during high-volatility states will reduce the incidence of severe adverse events and protocol violations compared to static-bound policies.
3. **Hypothesis 3 (Performance Tradeoff):** While the constrained agent may exhibit a marginally lower theoretical cumulative proximal reward on training data, its robust performance in minimizing severe psychiatric deteriorations (the "U-Curve" pitfall) will result in superior long-term clinical outcomes.

## Evaluation Strategy
To prove the efficacy of the proposed architecture, we will employ a rigorous simulation-based evaluation followed by an offline validation using historical clinical datasets.
- **Simulation Environment:** We will construct a synthetic psychiatric cohort simulation capable of simulating informative missingness and rapid state transitions (volatility) using the SDE-GAN and HDP-HMM framework.
- **Red-Teaming the RL Agent:** Following the methodology of Trella et al. (2024), we will systematically "stress-test" the agent in simulation to provoke fidelity failures and ensure the Dynamic Fidelity Controller correctly intervenes.
- **Off-Policy Evaluation (OPE):** We will validate the resulting policies using historical data from established datasets utilizing Marginalized Doubly Robust estimators to confirm the statistical validity of the proposed dynamic bounds.
