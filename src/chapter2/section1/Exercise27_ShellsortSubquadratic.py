#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-27 23:13:29
"""
Shellsort is Subquadratic
"""
import time

import tqdm


def shellsort(a):
    h = 1
    while h < len(a) // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h = h // 3


def insertionsort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def smoke_test_sort(sort):
    import random
    a = [random.randint(0, 10000) for _ in range(1000)]
    sort(a)

    assert sorted(a) == a


class StopWatch(object):
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def sort_compare(sort1, sort2, array_length, counts):
    total_time1 = 0.0
    total_time2 = 0.0

    # for _ in tqdm.trange(counts):
    for _ in range(counts):
        import random
        a = [random.randint(0, 10000) for _ in range(array_length)]
        a2 = a[:]

        watch = StopWatch()
        sort1(a)
        total_time1 += watch.stop()

        watch = StopWatch()
        sort2(a2)
        total_time2 += watch.stop()

    print("Total time for alg1: %.2f", total_time1)
    print("Total time for alg2: %.2f", total_time2)
    print("Alg1 takes %s time than alg2" % (total_time1 / total_time2))


if __name__ == '__main__':
    smoke_test_sort(shellsort)
    smoke_test_sort(insertionsort)

    length = 128
    while length < 4000:
        print("    Array length: %d" % length)
        sort_compare(shellsort, insertionsort, length, 100)
        length = 2 * length
