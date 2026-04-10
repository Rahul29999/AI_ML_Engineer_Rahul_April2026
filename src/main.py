import pandas as pd
import numpy as np
import json
from datetime import datetime

print("=== AI/ML Engineer Assessment 1: Multi-Agent War Room ===")
print("System started...\n")


def create_metrics():
    print("[TRACE] Creating mock dashboard metrics...")
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


def create_feedback():
    print("[TRACE] Loading user feedback...")
    return [
        "App is very slow",
        "Payment failed twice",
        "Great feature",
        "Amazing UI",
        "App crashes often",
        "Very buggy experience",
        "Feature is useful",
        "Slow response time",
        "Excellent update",
        "Facing login issue",
        "Login page freezes",
        "Too much lag",
        "Frequent app crash",
        "Checkout failed",
        "Very poor speed",
        "Feature adoption is easy",
        "Still facing errors",
        "Excellent functionality",
        "Customer support was helpful",
        "Payment timeout issue",
        "Loved the new checkout flow",
        "Frequent app crash on mobile",
        "Performance improved after retry",
        "Very poor loading speed"
    ]


def release_notes():
    return {
        "feature": "New Smart Checkout Feature",
        "known_risks": [
            "High backend API dependency",
            "Payment gateway timeout risk",
            "Possible mobile app crash on low-end devices"
        ]
    }


def detect_anomaly(series):
    print("[TOOL] detect_anomaly()")
    mean = np.mean(series)
    std = np.std(series)
    latest = series.iloc[-1]

    return {
        "status": "Anomaly Detected" if latest > mean + std else "Normal",
        "latest_value": float(latest),
        "mean": float(mean),
        "std": float(std)
    }


def trend_comparison(series):
    print("[TOOL] trend_comparison()")
    return {
        "start_value": float(series.iloc[0]),
        "end_value": float(series.iloc[-1]),
        "trend": "Decreasing" if series.iloc[-1] < series.iloc[0] else "Increasing"
    }


def sentiment_summary(feedback):
    print("[TOOL] sentiment_summary()")
    positive_words = ["great", "excellent", "amazing", "useful"]
    negative_words = ["slow", "failed", "crash", "issue", "lag", "poor"]

    pos = 0
    neg = 0

    for text in feedback:
        text = text.lower()

        if any(word in text for word in positive_words):
            pos += 1

        if any(word in text for word in negative_words):
            neg += 1

    return {"positive": pos, "negative": neg}


def main():
    print("[TRACE] Starting workflow...\n")

    metrics = create_metrics()
    feedback = create_feedback()
    notes = release_notes()

    pm_report = {
        "summary": "User adoption is falling",
        "metric_reference": trend_comparison(metrics["signup_conversion"])
    }

    data_report = {
        "crash_analysis": detect_anomaly(metrics["crash_rate"]),
        "latency_analysis": detect_anomaly(metrics["latency_p95"]),
        "ticket_trend": trend_comparison(metrics["support_tickets"])
    }

    marketing_report = sentiment_summary(feedback)

    risks = [
        "High crash risk",
        "High latency risk",
        "Negative customer sentiment"
    ] + notes["known_risks"]

    output = {
        "decision": "ROLL BACK",
        "rationale": {
            "pm": pm_report,
            "data": data_report,
            "marketing": marketing_report
        },
        "risk_register": risks,
        "action_plan_24_48_hours": [
            {"action": "Fix crash issue", "owner": "Engineering Team", "timeline": "24 hours"},
            {"action": "Improve API latency", "owner": "Backend Team", "timeline": "24 hours"},
            {"action": "Notify customers", "owner": "Marketing Team", "timeline": "48 hours"}
        ],
        "communication_plan": {
            "internal": "Escalate issue to leadership",
            "external": "Temporary rollback due to system instability"
        },
        "confidence_score": 0.91,
        "generated_at": str(datetime.now())
    }

    with open("outputs/output.json", "w") as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
