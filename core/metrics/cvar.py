"""Semantic CVaR."""
import numpy as np


def cvar(values):
    return float(np.mean(sorted(values)[-5:]))
