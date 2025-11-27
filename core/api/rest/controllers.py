from ..scoring import score


def evaluate_payload(payload):
    e = payload.get("entropy", 0.1)
    return {"score": score(e)}
