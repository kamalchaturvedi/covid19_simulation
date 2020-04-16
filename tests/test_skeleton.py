# -*- coding: utf-8 -*-

import pytest
from covid19_simulation.skeleton import fib

__author__ = "Kamal Chaturvedi"
__copyright__ = "Kamal Chaturvedi"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
