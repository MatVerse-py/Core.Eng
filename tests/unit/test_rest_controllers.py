from core.api.rest.controllers import evaluate_payload


def test_evaluate_payload_uses_entropy_value():
    assert evaluate_payload({"entropy": 0.25}) == {"score": 0.75}


def test_evaluate_payload_uses_default_entropy_when_missing():
    assert evaluate_payload({}) == {"score": 0.9}
