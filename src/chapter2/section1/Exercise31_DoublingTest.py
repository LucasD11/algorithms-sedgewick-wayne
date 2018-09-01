#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-09-01 19:32:33
"""
Doubling Test

Result(using pypy3):

For selection sort:
N=  1000, N^2=   1000000, Time=0.012797, Time/N^2=0.01280 * 10^(-6)
N=  2000, N^2=   4000000, Time=0.049987, Time/N^2=0.01250 * 10^(-6)
N=  3000, N^2=   9000000, Time=0.108801, Time/N^2=0.01209 * 10^(-6)
N=  4000, N^2=  16000000, Time=0.190332, Time/N^2=0.01190 * 10^(-6)
N=  5000, N^2=  25000000, Time=0.297019, Time/N^2=0.01188 * 10^(-6)
N=  6000, N^2=  36000000, Time=0.445400, Time/N^2=0.01237 * 10^(-6)
N=  7000, N^2=  49000000, Time=0.580701, Time/N^2=0.01185 * 10^(-6)
N=  8000, N^2=  64000000, Time=0.751289, Time/N^2=0.01174 * 10^(-6)
N=  9000, N^2=  81000000, Time=0.976115, Time/N^2=0.01205 * 10^(-6)
For insertion sort:
N=  1000, N^2=   1000000, Time=0.006542, Time/N^2=0.00654 * 10^(-6)
N=  2000, N^2=   4000000, Time=0.025686, Time/N^2=0.00642 * 10^(-6)
N=  3000, N^2=   9000000, Time=0.058173, Time/N^2=0.00646 * 10^(-6)
N=  4000, N^2=  16000000, Time=0.101060, Time/N^2=0.00632 * 10^(-6)
N=  5000, N^2=  25000000, Time=0.155953, Time/N^2=0.00624 * 10^(-6)
N=  6000, N^2=  36000000, Time=0.218928, Time/N^2=0.00608 * 10^(-6)
N=  7000, N^2=  49000000, Time=0.297869, Time/N^2=0.00608 * 10^(-6)
N=  8000, N^2=  64000000, Time=0.401239, Time/N^2=0.00627 * 10^(-6)
N=  9000, N^2=  81000000, Time=0.492774, Time/N^2=0.00608 * 10^(-6)
"""
import time
import random

TEST_TIMES = 10


def selection_sort(a):
    for i in range(len(a)):
        min_j = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def smoke_test(sort):
    a = [random.random() for _ in range(1000)]
    sort(a)
    assert sorted(a) == a


class StopWatch(object):
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def main(sort):
    n = 1000
    while n < 10000:
        total_time = 0.0
        for _ in range(TEST_TIMES):
            a = [random.random() for _ in range(n)]
            watch = StopWatch()
            sort(a)
            total_time += watch.stop()
        print("N=%6d, N^2=%10d, Time=%3.6f, Time/N^2=%5.5f * 10^(-6)" % (n, n**2, total_time, total_time / (n**2) * (10**6)))
        n += 1000


if __name__ == '__main__':
    smoke_test(selection_sort)
    smoke_test(insertion_sort)
    print("For selection sort:")
    main(selection_sort)
    print("For insertion sort:")
    main(insertion_sort)
