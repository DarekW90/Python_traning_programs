import random
import time


def naiveSearch(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binarySearch(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binarySearch(l, target, low, midpoint-1)
    else:
        return binarySearch(l, target, midpoint+1, high)


if __name__ == '__main__':

    length = 10000

    sortedList = set()
    while len(sortedList) < length:
        sortedList.add(random.randint(-3*length, 3*length))
    sortedList = sorted(list(sortedList))

    start = time.time()
    for target in sortedList:
        naiveSearch(sortedList, target)
    end = time.time()
    print('Naive search time: ', (end-start)*1000, 'milliseconds')

    start = time.time()
    for target in sortedList:
        binarySearch(sortedList, target)
    end = time.time()
    print('Binary search time: ', (end-start)*1000, 'milliseconds')
