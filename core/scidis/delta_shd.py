"""Compute ΔSHD."""

def delta_shd(baseline, new):
    return (baseline - new) / max(1e-9, baseline)
