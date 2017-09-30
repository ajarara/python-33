from thirtythree import start
from hypothesis import given
from hypothesis.strategies import integers

@given(integers())
def test_strong_simple(n):
    decomps = start.decompose(n, 1, strong=True)
    # there is only one way to decompose anything
    assert len(decomps) == 1

    for decomp in decomps:
        assert sum(decomp) == n


# idk how to enforce assumptions. don't make n too big or you'll
@given(integers(min_value=11, max_value=75),
       integers(min_value=1, max_value=10))
def test_strong(n, partitions):
    for decomp in start.decompose(n, partitions, strong=True):
        dec = tuple(decomp)
        assert tuple(reversed(sorted(dec))) == dec
        assert sum(dec) == n
        assert len(dec) == partitions


def test_strong_uses_same_ref():
    a = start.decompose(9, 3, strong=True)
    b = start.decompose(6, 2, strong=True)

    last_a = a[len(a) - 1]
    last_b = b[len(b) - 1]

    assert last_a.link is last_b
