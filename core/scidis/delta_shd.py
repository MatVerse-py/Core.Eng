"""Compute the proportional change in Structural Hamming Distance (ΔSHD)."""


def delta_shd(baseline, new):
    """Return the relative SHD reduction from ``baseline`` to ``new``.

    Args:
        baseline (float): Initial SHD value. Must be positive.
        new (float): SHD after an intervention.

    Raises:
        ValueError: If ``baseline`` is not strictly positive.
    """

    if baseline <= 0:
        raise ValueError("baseline must be positive to compute delta SHD")

    return (baseline - new) / baseline
