import pytest
from sample_package import Algorithm


def test_algorithm_class():
    """
    This is an example for a test which will pass.
    """
    algo = Algorithm(parameter_a=1)
    result = algo.calc(parameter_b=2)
    assert result == 3


def test_2_algorithm_class():
    """
    And an example of a test which will fail.
    """
    algo = Algorithm(parameter_a=1)
    result = algo.calc(parameter_b=2)
    assert result == 4


@pytest.mark.parametrize("parameter_b, expected_result", [(1, 2), (2, 3)])
def test_parametrized_algorithm_class(parameter_b, expected_result):
    """
    An example of a parameterized test. It runs the test multiple times by passing the arguments
    given by `@pytest.mark.parametrize()`.
    """
    algo = Algorithm(parameter_a=1)
    result = algo.calc(parameter_b)
    assert result == expected_result
