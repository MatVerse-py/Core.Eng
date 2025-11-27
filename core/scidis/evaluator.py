"""Scientific evaluator."""
from .delta_shd import delta_shd


class Evaluator:
    def run(self, data):
        return {"shd": delta_shd(data[0], data[1])}
