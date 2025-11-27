"""
QUCA: orchestrates cognitive subsystems.
"""
from .state_sync import sync_states
from ..cnd.cnd_engine import CND
from ..scdi.scdi_core import SCDI


class QUCA:
    def __init__(self):
        self.cnd = CND()
        self.scdi = SCDI()

    def tick(self):
        entropy = self.cnd.consume_noise()
        decision = self.scdi.evaluate(entropy)
        sync_states()
        return decision
