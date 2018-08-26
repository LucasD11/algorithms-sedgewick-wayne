#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-26 21:27:50
"""
Insertion Sort with Sentinel
"""

import time
import random

import tqdm


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def insertion_sort_sentinel(a):
    min_i = 0
    for i in range(1, len(a)):
        if a[i] < a[min_i]:
            min_i = i
    a[min_i], a[0] = a[0], a[min_i]
    for i in range(1, len(a)):
        j = i
        while a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def smoke_test_sort(sort):
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
    for _ in tqdm.trange(counts):
        a1 = [random.randint(0, 10000) for _ in range(array_length)]
        a2 = a1.copy()

        watch = StopWatch()
        sort1(a1)
        total_time1 += watch.stop()

        watch= StopWatch()
        sort2(a2)
        total_time2 += watch.stop()

    print("Total time for arg1: %.2f" % total_time1)
    print("Total time for arg2: %.2f" % total_time2)
    print("Is %f times than arg2" % (total_time1 / total_time2))


if __name__ == '__main__':
    smoke_test_sort(insertion_sort)
    smoke_test_sort(insertion_sort_sentinel)
    sort_compare(insertion_sort, insertion_sort_sentinel, 1000, 100)
