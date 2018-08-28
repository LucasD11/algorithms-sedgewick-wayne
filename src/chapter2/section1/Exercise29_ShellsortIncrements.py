#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-28 23:18:43
"""
Shellsort Increments
"""
import time
import random


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


def shellsort2(a):
    """
    Shellsort with increments 1, 5, 19, 41, 109. Which is the combination of `9*4^k - 9*2^k + 1`
    and `4^k - 3*2^k + 1`
    """
    sequence1 = []
    sequence2 = []
    k = 0
    while not sequence1 or sequence1[-1] < len(a) // 3:
        sequence1.append(9 * 4 ** k - 9 * 2 ** k + 1)
        k += 1
    k = 2
    while not sequence2 or sequence2[-1] < len(a) // 3:
        sequence2.append(4 ** k - 3 * 2 ** k + 1)
        k += 1
    sequence = sorted(sequence1 + sequence2)

    for h in sequence[::-1]:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h


class StopWatch:
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def compare_sort(sort1, sort2, counts):
    total_time1 = 0.0
    total_time2 = 0.0
    length = 128
    while max(total_time1, total_time2) < 10:
        total_time1 = 0.0
        total_time2 = 0.0
        for _ in range(counts):
            a = [random.randint(0, 100000) for _ in range(length)]
            a2 = a[:]

            watch = StopWatch()
            sort1(a)
            total_time1 += watch.stop()

            watch = StopWatch()
            sort2(a2)
            total_time2 += watch.stop()
        print(
            "For length %6d, arg1 uses %3.4f and arg2 uses %3.4f. Arg1 takes %4.4f than arg2" % (
                length, total_time1, total_time2, total_time1 / total_time2
            )
        )
        length = 2 * length


def smoke_test(sort):
    a = [random.randint(0, 10000) for _ in range(5000)]
    sort(a)
    assert sorted(a) == a


if __name__ == '__main__':
    smoke_test(shellsort)
    smoke_test(shellsort2)
    compare_sort(shellsort, shellsort2, 10)
