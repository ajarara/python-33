from thirtythree import decompositions as dc
from hypothesis import given
from hypothesis.strategies import integers

@given(integers())
def test_strong_simple(n):
    decomps = dc.strong_decompose(n, 1)
    # there is only one way to decompose anything
    assert len(decomps) == 1

    for decomp in decomps:
        assert sum(decomp) == n


# idk how to enforce assumptions. don't make n too big or you'll
@given(integers(min_value=11, max_value=75),
       integers(min_value=1, max_value=10))
def test_strong(n, partitions):
    for decomp in dc.strong_decompose(n, partitions):
        dec = tuple(decomp)
        assert tuple(reversed(sorted(dec))) == dec
        assert sum(dec) == n
        assert len(dec) == partitions


def test_strong_uses_same_ref():
    a = dc.strong_decompose(9, 3)
    b = dc.strong_decompose(6, 2)

    last_a = a[len(a) - 1]
    last_b = b[len(b) - 1]

    assert last_a.link is last_b
