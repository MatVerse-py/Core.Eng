from core.metrics.ci_t import ci_t


def test_ci_t_within_bounds():
    assert ci_t(0.2) == 0.8


def test_ci_t_clamps_lower_and_upper():
    assert ci_t(2) == 0
    assert ci_t(-0.5) == 1
