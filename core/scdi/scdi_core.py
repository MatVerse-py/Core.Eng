"""
SCDI: coherent decision maker.
"""
from .scoring import score


class SCDI:
    def evaluate(self, entropy):
        return score(entropy)
