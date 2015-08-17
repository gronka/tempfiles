#linked list strategy
# collect first k items
# 1) when finding max for index i, drop the element at i -k
# 2) add the value at i
# 3) find the max
# 4) calculate for k + 1

import collections
def fifo(vals, k):
    retList = []*(len(vals)-k)
    maxVal = 0
    i = 0
    #TODO: does not work for negative value lists
    window = collections.deque(k*[0], k)
    for i in range(0, k):
        window.appendleft(vals[i])
    retList.append(max(window))

    for i in range(i+1, len(vals)):
        lastVal = window[-1]
        window.appendleft(vals[i])
        if vals[i] > maxVal:
            # if new value is greater, assign it
            maxVal = vals[i]
        elif lastVal == maxVal:
            # if we lost the old maxVal, find max()
            maxVal = max(window)
        retList.append(maxVal)
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

def mymax(mylist):
    return max(mylist)

#def fmiw_gen(nums, window):
    #for i in range(window, len(nums)):
        #yield (nums[i-window], nums[i], nums)
    # squares = map(lambda x: x**2, range(10))

def simple_max(vals):
    return max(vals)


if __name__ == "__main__":
    # nums = [ 8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    # fmiw(nums, 3)
    # print(map(mylist, nums))

    k = 3
    myFIFO = WrapFIFO(k)

    vals = [10, 0, 1, 3, 6, 9, 2, 4, 6, 8, 10]
    for val in vals:
        myFIFO.append(val)
        # print(str(myFIFO.getMax()))

    # newList = window_iter(3, vals)
    # print(newList)


    from timeit import Timer

    import random
    vals = random.sample(range(10000), 10000)

    k = 8
    t0 = Timer(lambda: simple_max(vals))
    t1 = Timer(lambda: fifo(vals, k))
    t2 = Timer(lambda: list_slice(vals, 3))

    _NUMBER = 1000
    print("{0} simple_max: {1}".format(_NUMBER, t0.timeit(number=_NUMBER)))
    print("{0} fifo: {1}".format(_NUMBER, t1.timeit(number=_NUMBER)))
    print("{0} list_slice: {1}".format(_NUMBER, t2.timeit(number=_NUMBER)))




