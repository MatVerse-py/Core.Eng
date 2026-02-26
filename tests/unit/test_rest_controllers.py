import pytest

from core.api.rest.controllers import evaluate_payload


def test_evaluate_payload_uses_entropy_value():
    assert evaluate_payload({"entropy": 0.25}) == {"score": 0.75}


def test_evaluate_payload_uses_default_entropy_when_missing():
    assert evaluate_payload({}) == {"score": 0.9}


def test_evaluate_payload_accepts_none_payload_as_default_entropy():
    assert evaluate_payload(None) == {"score": 0.9}


def test_evaluate_payload_coerces_numeric_entropy_strings():
    assert evaluate_payload({"entropy": "0.4"}) == {"score": 0.6}


@pytest.mark.parametrize(
    "payload",
    [
        {"entropy": -0.1},
        {"entropy": "invalid"},
        123,
    ],
)
def test_evaluate_payload_rejects_invalid_payloads(payload):
    with pytest.raises(ValueError):
        evaluate_payload(payload)
