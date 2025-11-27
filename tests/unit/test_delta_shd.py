from core.scidis.delta_shd import delta_shd
import pytest


def test_delta_shd():
    assert delta_shd(10, 5) == 0.5


def test_delta_shd_requires_positive_baseline():
    with pytest.raises(ValueError):
        delta_shd(0, 5)


def test_delta_shd_handles_increase():
    assert delta_shd(4, 6) == -0.5
