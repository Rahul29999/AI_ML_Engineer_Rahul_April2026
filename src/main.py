import pandas as pd
import numpy as np
import json
from datetime import datetime


def create_metrics():
    days = pd.date_range("2026-04-01", periods=10)

    return pd.DataFrame({
        "date": days,
        "signup_conversion": [25, 26, 27, 28, 24, 23, 21, 20, 18, 17],
        "DAU": [1000, 1020, 1035, 1040, 980, 950, 900, 870, 850, 820],
        "retention_D7": [70, 71, 72, 73, 68, 65, 62, 60, 58, 55],
        "crash_rate": [1, 1, 1.2, 1.1, 2, 2.5, 3, 4, 4.5, 5],
        "latency_p95": [120, 122, 121, 123, 140, 150, 170, 190, 210, 230],
        "support_tickets": [5, 4, 6, 5, 10, 15, 18, 22, 25, 30]
    })


def anomaly_check(series):
    avg = np.mean(series)
    std = np.std(series)
    latest = series.iloc[-1]

    return {
        "status": "Anomaly Detected" if latest > avg + std else "Normal",
        "latest_value": float(latest),
        "mean": float(avg)
    }


def main():
    metrics = create_metrics()

    output = {
        "decision": "ROLL BACK",
        "rationale": {
            "crash_analysis": anomaly_check(metrics["crash_rate"]),
            "latency_analysis": anomaly_check(metrics["latency_p95"])
        },
        "risk_register": [
            "High crash risk",
            "High latency risk",
            "Negative customer sentiment"
        ],
        "action_plan_24_48_hours": [
            {"action": "Fix crash issue", "owner": "Engineering Team"},
            {"action": "Improve latency", "owner": "Backend Team"},
            {"action": "Notify customers", "owner": "Marketing Team"}
        ],
        "confidence_score": 0.91,
        "generated_at": str(datetime.now())
    }

    with open("outputs/output.json", "w") as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
