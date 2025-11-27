"""Gate API."""
from ..omegagate.gate_logic import approve


def gateway(score):
    return approve(score)
