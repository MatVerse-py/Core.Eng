"""Temporal Coherence Index.

The score represents how coherent a process remains over time given an
entropy estimate. Entropy values outside the expected ``[0, 1]`` interval are
clamped so the result always stays between 0 and 1.
"""


def ci_t(entropy):
    """Return the temporal coherence index clamped to the ``[0, 1]`` range."""

    coherence = 1 - entropy
    if coherence < 0:
        return 0
    if coherence > 1:
        return 1
    return coherence
