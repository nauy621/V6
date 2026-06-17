def analyze(state):
    history = state["history"]

    if len(history) < 2:
        return {"trend": 0, "week_7": history[-1]}

    trend = (history[-1] - history[-2])

    week_7 = history[-1] + trend * 7

    return {
        "trend": trend,
        "week_7": week_7
    }
