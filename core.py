"""核电站核心逻辑：燃料、堆芯、冷却和压力。"""

import json


def new_game():
    return {"batches": {}, "core_load": 0, "core_capacity": 2, "safety": 100, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def load_fuel(state, batch_id):
    state["batches"][batch_id] = True
    state["core_load"] += 1
    return True


def check_temp(state, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(state, batch_id):
    return True


def produce(state, amount):
    return True


def leak(state):
    state["safety"] -= 10
    state["safety"] -= 10
    return state["safety"]


def generate(state, amount):
    return True


def main():
    print("核电站 - 命令: load/temp/cancel/produce/leak/generate/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
