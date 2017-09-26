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
        raise StopIteration

    # these two dunders are needed for caching mechanisms
    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, other):
        if self.link is None and other.link is None:
            return True
        elif None in (self.link, other.link):
            return False
        else:
            return self.val == other.val and self.link == other.link


def strong_decompose(n, partitions):
    if partitions == 1:
        yield Node(n)
    else:
        for hd in reversed(range(1, n - partitions + 2)):
            for tl in strong_decompose(n - hd, partitions - 1):
                # eh... good enough.
                if hd >= tl.val:
                    yield Node(hd, tl)


def weak_decompose(n, partitions):
    if partitions == 1:
        yield Node(n)
    else:
        for hd in reversed(range(n + 1)):
            for tl in weak_decompose(n - hd, partitions - 1):
                if hd >= tl.val:
                    yield Node(hd, tl)


def factorial(n):
    def fact_help(n, running):
        if n == 1:
            return running
        return fact_help(n - 1, running * n)
    return fact_help(n, 1)


def permutations(n, r):
    return factorial(n) // factorial(n - r)


def combinations(n, r):
    return permutations(n, r) // factorial(r)


# doesn't work.
# this... is a complicated problem. gonna whiteboard it a bit.
def weak_decompose_cached(n, partitions, _cache={}):
    if partitions == 1:
        if (n, partitions) not in _cache:
            _cache[n, partitions] = [Node(n)]
        for decomp in _cache[n, partitions]:
            yield decomp
    else:
        for hd in reversed(range(n + 1)):
            recur = (n - hd, partitions - 1)
            for tl in weak_decompose(*recur):
                if hd >= tl.val:
                    if recur not in _cache and _cache[recur]:
                        _cache[recur] = Node(hd, tl)
                    yield _cache[recur]
