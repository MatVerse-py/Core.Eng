"""
Core cognitive kernel.
Implements task scheduling, state loops, and QUCA sync hooks.
"""
import time
from ..quca.state_sync import sync_states


class Kernel:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            sync_states()
            time.sleep(0.01)
