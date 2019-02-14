import pytest

import easy

def test_perimetr():
    t1 = easy.Triangle([0, 0], [2, 2], [4, 0])
    assert t1.perimetr() == 9.65685424949238