import json

FILE = "storage.json"

def load_state():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {
            "weight": 75,
            "fatigue": 50,
            "recovery": 50,
            "history": [75]
        }

def save_state(state):
    with open(FILE, "w") as f:
        json.dump(state, f)

def update_state(state, mode):
    if mode == "train":
        state["fatigue"] += 10
        state["recovery"] -= 5
        state["weight"] -= 0.2

    if mode == "rest":
        state["fatigue"] -= 15
        state["recovery"] += 15

    state["fatigue"] = max(0, min(100, state["fatigue"]))
    state["recovery"] = max(0, min(100, state["recovery"]))

    state["history"].append(state["weight"])

    save_state(state)
    return state

def get_today_plan():
    import datetime
    weekday = datetime.datetime.now().weekday()

    training = [
        "胸 + 三头",
        "背 + 二头",
        "腿 + 核心",
        "肩 + 手臂",
        "轻全身",
        "燃脂",
        "恢复"
    ]

    diet = [
        "热干面 + 鸡蛋",
        "蒸饺 + 鸡蛋",
        "热干面 + 鸡蛋",
        "蒸饺 + 鸡蛋",
        "鸡胸肉轻食",
        "轻食控制",
        "自由但不暴食"
    ]

    return {
        "training": training[weekday],
        "diet": diet[weekday]
    }
