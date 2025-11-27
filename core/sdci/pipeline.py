"""
Operational pipeline.
"""


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, x):
        for fn in self.steps:
            x = fn(x)
        return x
