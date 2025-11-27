"""Decision scoring based on entropy and CI_t."""

def score(entropy):
    return max(0.0, 1.0 - entropy)
