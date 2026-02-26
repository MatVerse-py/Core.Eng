from collections.abc import Mapping

from ...scdi.scoring import score

_DEFAULT_ENTROPY = 0.1


def _coerce_entropy(value) -> float:
    """Normalize entropy input into a non-negative float."""
    try:
        entropy = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("entropy must be a numeric value") from exc

    if entropy < 0:
        raise ValueError("entropy must be non-negative")

    return entropy


def evaluate_payload(payload: Mapping[str, object] | None) -> dict[str, float]:
    """Compute score from payload data with explicit input validation."""
    if payload is None:
        entropy = _DEFAULT_ENTROPY
    elif isinstance(payload, Mapping):
        entropy = _coerce_entropy(payload.get("entropy", _DEFAULT_ENTROPY))
    else:
        raise ValueError("payload must be a mapping or None")

    return {"score": score(entropy)}
