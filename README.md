# AI/ML Engineer Assessment Submission  
**Candidate:** Rahul Kumar Sharma  
**Role:** AI / ML Engineer  
**Assessment:** Multi-Agent Launch War Room  

---

## Project Overview
This project simulates a **cross-functional product launch war room** used during a feature rollout.

The system analyzes business metrics, technical performance indicators, customer feedback, and known release risks to generate a structured launch decision:

- **PROCEED**
- **PAUSE**
- **ROLL BACK**

The solution follows a **multi-agent decision workflow**, where each agent is responsible for a specific business function.

---

## Problem Statement
During a new product launch, multiple metrics may shift unexpectedly.

The objective of this system is to simulate how product, engineering, analytics, and marketing teams collaborate in a war room environment to decide whether the rollout should continue.

---

## Agents Implemented
The workflow simulates the following agents:

### 1. Product Manager Agent
Responsible for:
- adoption trend analysis
- user impact evaluation
- launch success criteria

### 2. Data Analyst Agent
Responsible for:
- crash anomaly detection
- latency spike detection
- ticket trend analysis
- metric comparisons

### 3. Marketing Agent
Responsible for:
- customer sentiment analysis
- positive vs negative feedback tracking

### 4. Risk Critic Agent
Responsible for:
- identifying deployment risks
- validating rollout safety
- highlighting failure points

### 5. Coordinator Agent
Responsible for:
- consolidating agent outputs
- final launch decision
- confidence scoring

---

## Tools / Functions Used
The following programmatic tools are used by agents:

- `detect_anomaly()`
- `trend_comparison()`
- `sentiment_summary()`

These are invoked directly by agents during the decision workflow.

---

## Input Artifacts
Located in `/data`

### Files
- `mock_metrics.csv`
- `user_feedback.txt`
- `release_notes.json`

### Metrics Included
- Signup Conversion
- Daily Active Users
- D7 Retention
- Crash Rate
- p95 API Latency
- Support Tickets

---

## Output
Generated inside `/outputs`

### File
`output.json`

Contains:
- decision
- rationale
- risk register
- action plan
- communication plan
- confidence score

---

## Project Structure
```text
src/        -> main application code
data/       -> input artifacts
outputs/    -> generated JSON output
notebook/   -> Jupyter notebook workflow
demo/       -> video link / demo artifact
```

---

## Installation
```bash
pip install -r requirements.txt
```

---

## Run Instructions
```bash
python src/main.py
```

---

## Example Final Decision
```json
{
  "decision": "ROLL BACK"
}
```

---

## Demo Video
Demo video link available inside:

```text
demo/demo_video_link.txt
```

---

## Tech Stack
- Python
- Pandas
- NumPy
- JSON
- Jupyter Notebook

---

## Notes
No external APIs or keys are required.

The solution is fully reproducible using Python.
