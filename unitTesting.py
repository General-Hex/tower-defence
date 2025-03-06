"""
Secondary module used for unit testing
"""

import pytest

def square(a):
    return a*a

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-1) == 1

