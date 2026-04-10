# AI/ML Engineer Assessment Submission  
**Candidate:** Rahul Kumar Sharma  
**Role:** AI / ML Engineer  
**Assessment:** Multi-Agent Launch War Room  

## Project Overview
This project simulates a **cross-functional product launch war room** used during a feature rollout.

The system analyzes:
- business metrics
- technical performance indicators
- customer feedback
- known release risks

and produces a structured launch decision:

- **PROCEED**
- **PAUSE**
- **ROLL BACK**

The workflow follows a **multi-agent orchestration approach**, where each agent represents a specific business function.


## Problem Statement
During a new product launch, multiple business and technical metrics may shift unexpectedly.

The objective of this project is to simulate how product, engineering, analytics, and marketing teams collaborate in a war room environment to decide whether the rollout should continue.


## Agents Implemented
The system includes the following agents:

### 1. Product Manager Agent
Responsible for:
- adoption trend analysis
- success criteria validation
- user impact review

### 2. Data Analyst Agent
Responsible for:
- crash anomaly detection
- latency spike analysis
- support ticket trend monitoring
- metric comparison

### 3. Marketing Agent
Responsible for:
- customer sentiment analysis
- positive vs negative feedback review

### 4. Risk Critic Agent
Responsible for:
- identifying deployment risks
- validating rollout safety
- highlighting failure points

### 5. Coordinator Agent
Responsible for:
- consolidating all agent outputs
- generating final launch decision
- assigning confidence score


## Tools / Functions Used
The following tools are invoked programmatically by agents:

- `detect_anomaly()`
- `trend_comparison()`
- `sentiment_summary()`

These tools are used during the decision workflow.


## Input Artifacts
Located in `data/`

### Files
- `mock_metrics.csv`
- `user_feedback.txt`
- `release_notes.json`

### Metrics Covered
- Signup Conversion
- Daily Active Users
- D7 Retention
- Crash Rate
- p95 API Latency
- Support Ticket Volume


## Output
Generated in `outputs/output.json`

Contains:
- decision
- rationale
- risk register
- action plan (24–48 hours)
- communication plan
- confidence score


## Project Structure
```text
src/        -> source code
data/       -> input artifacts
outputs/    -> generated JSON output
notebook/   -> Jupyter notebook workflow
demo/       -> video link
```


## Installation
```bash
pip install -r requirements.txt
```


## Run Instructions
```bash
python src/main.py
```


## Example Final Decision
```json
{
  "decision": "ROLL BACK"
}
```


## Demo Video
[Click here to watch the demo video](https://drive.google.com/file/d/1Uq-S9dj65zpOuzYJg_eedaBfAZUF6Ubz/view?usp=sharing)

## Tech Stack
- Python
- Pandas
- NumPy
- JSON
- Jupyter Notebook


## Notes
No external APIs or keys are required.

The solution is fully reproducible using Python.
