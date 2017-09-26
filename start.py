
class Node(object):
    def __init__(self, val, link):
        self.val = val
        self.link = link

    def __repr__(self):
        return "({} . {})".format(self.val, repr(self.link))

    def __iter__(self):
        here = self
        while here is not None:
            yield here.val
            here = here.link
        raise StopIteration


def strong_decompose(n, partitions):
    if partitions == 1:
        yield Node(n, None)
    else:
        for hd in reversed(range(1, n - partitions + 2)):
            for tl in strong_decompose(n - hd, partitions - 1):
                if hd >= tl.val:
                    yield Node(hd, tl)
