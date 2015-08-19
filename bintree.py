# from bintree import FastRBTree
import bintree

def simple_max(vals):
    return max(vals)

class bWrap(RBTree):
    def __init__(self):
        super().__init__()
        duplicates = {}


def run_bintree(vals, k):
    t = bWrap()
    t[vals[0]] = 0
    for i in range(1, k):
        if t.item(t.index(vals[i])):
            print("key is already defined")
        t[vals[i]] = i


if __name__ == "__main__":
    _RUNS = 1
    import random
    vals = random.sample(range(1000), 1000)
    k = 8

    from timeit import Timer
    t0 = Timer(lambda: simple_max(vals))
    t1 = Timer(lambda: run_bintree(vals, k))

    print("{0} simple_max: {1}".format(_RUNS, t0.timeit(number=_RUNS)))
    print("{0} run_bintree: {1}".format(_RUNS, t1.timeit(number=_RUNS)))
