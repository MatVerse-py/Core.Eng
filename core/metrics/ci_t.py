"""Temporal Coherence Index."""

def ci_t(entropy):
    return max(0, 1 - entropy)
