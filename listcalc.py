#linked list strategy
# collect first k items
# 1) when finding max for index i, drop the element at i -k
# 2) add the value at i
# 3) find the max
# 4) calculate for k + 1

import collections
#TODO: functions will break if k < len(vals)
def fifo(vals, k):
    retList = []*(len(vals)-k)
    maxVal = 0
    i = 0
    #TODO: does not work for negative value lists
    window = collections.deque(k*[0], k)
    for i in range(0, k):
        window.appendleft(vals[i])
    maxVal = max(window)
    retList.append(maxVal)

    for i in range(k, len(vals)):
        lastVal = window[-1]
        window.appendleft(vals[i])
        if vals[i] > maxVal:
            # if new value is greater, assign it
            maxVal = vals[i]
        elif lastVal == maxVal:
            # if we lost the old maxVal, find max()
            maxVal = max(window)
        retList.append(maxVal)
    # print(retList)
    # print("len(retList):" + str(len(retList)))
    return retList


class WrapFIFO():
    def __init__(self, k):
        self.max = 0
        #TODO: initialize this for negative values?
        self.window = collections.deque(k*[0], k)

    def append(self, val):
        lastVal = self.window[-1]
        self.window.appendleft(val)
        if lastVal == self.max:
            self.max = max(self.window)
        elif val > self.max:
            self.max = val

    def getMax(self):
        return self.max


def list_slice(nums, k):
    retList = []
    for i in range(len(nums)):
        # newlist = nums[i:i+k]
        if i+k > len(nums):
            break
        retList.append(max(nums[i:i+k]))

        # assert(len(newlist) == k)
        # print(max(newlist))
        #print(str(newlist))
    # print(retList)
    # print("len(retList):" + str(len(retList)))
    return retList


def map_slice(nums, k):
    retList = []
    for i in range(len(nums)):
        if i+k > len(nums):
            break
        retList.append(map(lambda x: max(x), nums[i:i+k]))

def mymax(mylist):
    return max(mylist)

#def fmiw_gen(nums, window):
    #for i in range(window, len(nums)):
        #yield (nums[i-window], nums[i], nums)
    # squares = map(lambda x: x**2, range(10))

def simple_max(vals):
    return max(vals)


def double_deck(vals, k):
    retList = []*(len(vals)-k)
    i = 0
    #TODO: does not work for negative value lists
    maxVal = collections.deque()
    maxIdx = collections.deque()

    maxVal.append(vals[0])
    maxIdx.append(0)
    for i in range(1, k):
        # if maxIdx[0] ==
        if vals[i] > maxVal[-1]:
            maxVal.append(vals[i])
            maxIdx.append(i)

    retList.append(maxVal[-1])
    for i in range(k, len(vals)):
        try:
            if maxIdx[0] == i - k:
                maxIdx.popleft()
                maxVal.popleft()
        except:
            pass
        try:
            if vals[i] > maxVal[-1]:
                maxVal.append(vals[i])
                maxIdx.append(i)
        except IndexError:
            maxVal.append(vals[i])
            maxIdx.append(i)
        retList.append(maxVal[-1])
    for i in range(0, len(maxVal)):
        # print(maxVal[i])
        # print(maxIdx[i])
        pass
    # print(retList)
    # print("len(retList):" + str(len(retList)))
    return retList

def single_deck(vals, k):
    # print(vals)
    # print(str(k))
    retList = []*(len(vals)-k)
    i = 0
    #TODO: does not work for negative value lists
    maxVal = collections.deque()

    maxVal.append({"idx": 0, "val": vals[0]})
    # print(maxVal[0].keys())
    for i in range(1, k):
        if vals[i] > maxVal[-1]["val"]:
            maxVal.append({"idx": i, "val": vals[i]})

    retList.append(maxVal[-1]["val"])
    # print("current retList:")
    # print(retList)
    for i in range(k, len(vals)):
        if maxVal[0]["idx"] == i - k:
            maxVal.popleft()
        try:
            if vals[i] > maxVal[-1]["val"]:
                maxVal.append({"idx": i, "val": vals[i]})
        except IndexError:
            # basically, if deque is empty
            maxVal.append({"idx": i, "val": vals[i]})
        retList.append(maxVal[-1]["val"])
        # print(retList)
    # print("final retList:")
    # print(retList)
    # print("len(retList):" + str(len(retList)))
    return retList

from itertools import islice
def islice_method(vals, k):
    retList = []*(len(vals)-k)
    slices = zip(*(islice(vals, i, None) for i in range(k)))
    for slice_ in slices:
        retList.append(max(slice_))
    return retList


if __name__ == "__main__":
    import sys
    import random
    try:
        if sys.argv[1] == "test" or sys.argv[1] == "t":
            k = 5
            vals = random.sample(range(30), 30)
            print("vals:")
            print(vals)
            print("fifo:")
            print(fifo(vals, k))
            print("double_deck:")
            print(double_deck(vals, k))
            print("islice_method:")
            print(islice_method(vals, k))

        if sys.argv[1] == "speed" or sys.argv[1] == "s":
            from timeit import Timer
            vals = random.sample(range(1000000), 1000000)
            for i in range(1, 4):
                k = 40*i
                print("_________ k = {0} ________".format(k))
                t0 = Timer(lambda: simple_max(vals))
                t1 = Timer(lambda: fifo(vals, k))
                t2 = Timer(lambda: list_slice(vals, k))
                t3 = Timer(lambda: double_deck(vals, k))
                t4 = Timer(lambda: single_deck(vals, k))
                t5 = Timer(lambda: islice_method(vals, k))

                _RUNS = 1
                print("{0} simple_max: {1}".format(_RUNS, t0.timeit(number=_RUNS)))
                print("{0} fifo: {1}".format(_RUNS, t1.timeit(number=_RUNS)))
                print("{0} list_slice: {1}".format(_RUNS, t2.timeit(number=_RUNS)))
                print("{0} double_deck: {1}".format(_RUNS, t3.timeit(number=_RUNS)))
                print("{0} single_deck: {1}".format(_RUNS, t4.timeit(number=_RUNS)))
                print("{0} islice_method: {1}".format(_RUNS, t5.timeit(number=_RUNS)))
    except IndexError:
        print("To test accurracy, pass argument 't' or 'test'")
        print("To test speed, pass argument 's' or 'speed'")
        print("Examples:")
        print("python listcalc.py t")
        print("python listcalc.py s")







