# mHealth Engagement Schemas (mindLAMP & RADAR-base)

## 📄 Definition
Technical schemas for tracking user interaction with mobile health platforms. These schemas provide the raw telemetry required for [[engagement_validation]] and [[digital_phenotyping]].

## 🛠️ Feature Schemas

### mindLAMP (Engagement Analytics)
Focuses on the lifecycle of a notification and user interaction:
- `notification.delivered`: Timestamp when the prompt reached the device.
- `notification.opened`: Timestamp of user interaction.
- `notification.dismissed`: User explicitly cleared the notification without opening.
- `interaction_latency`: Time delta between delivery and opening (used as a marker for psychomotor speed).

### RADAR-base (Application Notification Event)
Standardized Avro schema for large-scale clinical trials:
- `state`: `SCHEDULED`, `DELIVERED`, `OPENED`, `DISMISSED`.
- `type`: Category of prompt (`ESM`, `JITAI_NUDGE`, `REMINDER`).
- `timeReceived`: Handset-level receipt confirmation.

## 🔬 Clinical Markers Derived from Schemas
- **Prompt Sensitivity:** Ratio of `opened` to `delivered` notifications.
- **Engagement Window:** Identifying "optimal times" for interaction (e.g., 9 AM vs. 11 PM).
- **The "Dismissal" Signal:** High dismissal rates as a proxy for **Digital Exhaustion** or **Autonomy Pressure**.

## 🩺 Clinical Validation
- **DWAI Correlation:** High scores in the 'Bond' subscale of the [[digital_navigator]] alliance inventory correlate with lower `interaction_latency` and higher sensor coverage (steps, heart rate).
- **Psychomotor Retardation:** Increased latency is a validated digital biomarker for MDD symptom severity.

## 🔗 Related Concepts
- [[engagement_validation]]
- [[digital_navigator]]
- [[digital_phenotyping]]
- [[behavioral_theories]]
