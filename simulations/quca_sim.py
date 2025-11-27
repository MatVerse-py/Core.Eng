"""Simulador QUCA + CND"""
from core.quca.quca_engine import QUCA


def run():
    q = QUCA()
    for _ in range(10): print(q.tick())
