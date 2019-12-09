import pytest

from optsml.statistics.averages import MovingAverages


def test_simple_moving_average():
    mavg = MovingAverages()
    res = mavg.simple_moving_average([1, 2, 3, 4])
    assert res != 0
