from thirtythree import start
from hypothesis import given
from hypothesis.strategies import integers

@given(integers())
def test_strong_simple(n):
    decomps = start.strong_decompose(n, 1)
    # there is only one way to decompose anything
    assert len(decomps) == 1

    for decomp in decomps:
        assert sum(decomp) == n

@given(integers(), integers())
def test_multi_part(n, partitions):
    
