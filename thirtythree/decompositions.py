class Node(object):
    def __init__(self, val, link=None):
        self.val = val
        if link is not None:
            assert isinstance(link, Node)
        self.link = link

    def __repr__(self):
        return "({} . {})".format(self.val, repr(self.link))

    def __iter__(self):
        here = self
        while here is not None:
            yield here.val
            here = here.link


def memoize(fun):
    cache = {}

    def memoized_fun(*args, **kwargs):
        if args not in cache:
            cache[args] = tuple(fun(*args, **kwargs))
        return cache[args]
    return memoized_fun


@memoize
def strong_decompose(n, partitions):
    if partitions == 1:
        yield Node(n)
    else:
        for hd in reversed(range(1, n - partitions + 2)):
            for tl in strong_decompose(n - hd, partitions - 1):
                if hd >= tl.val:
                    yield Node(hd, tl)


@memoize
def weak_decompose(n, partitions):
    if partitions == 1:
        yield Node(n)
    else:
        for hd in reversed(range(n + 1)):
            for tl in weak_decompose(n - hd, partitions - 1):
                if hd >= tl.val:
                    yield Node(hd, tl)


def factorial(n):
    assert isinstance(n, int)
    assert n >= 0

    running = 1
    while n > 1:
        running *= n
        n -= 1
    return running


def permutations(n, r):
    return factorial(n) // factorial(n - r)


def combinations(n, r):
    return permutations(n, r) // factorial(r)
