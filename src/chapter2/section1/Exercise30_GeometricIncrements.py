#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-09-01 18:49:52
"""
Geometric Increments

Using pypy to run this algorithm so that it is not too slow

Result::

   Total time: 9.0895, when t=2
   Total time: 9.0692, when t=3
   Total time: 10.2303, when t=4
   Total time: 10.3432, when t=5
   Total time: 10.2500, when t=6
   Total time: 12.2262, when t=7
   Total time: 13.8888, when t=8
   Total time: 11.9126, when t=9
   pypy3 Exercise30_GeometricIncrements.py  86.30s user 0.64s system 99% cpu 1:27.80 total
"""
import time
import random

CASE_LEN = 1000000
CASE_NUMBERS = 5


def shell_sort_factory(t):
    def shell_sort(a):
        sequence = [1]
        k = 1
        while sequence[-1] < len(a) // 3:
            sequence.append(t**k)
            k += 1

        for h in sequence[::-1]:
            for i in range(h, len(a)):
                j = i
                while j >= h and a[j] < a[j-h]:
                    a[j], a[j-h] = a[j-h], a[j]
                    j -= h
    return shell_sort


def smoke_test(sort):
    a = [random.random() for _ in range(CASE_LEN)]
    sort(a)
    assert sorted(a) == a
    print(len(a))


class StopWatch(object):
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def main():
    cases = [
        [random.random() for _ in range(CASE_LEN)] for _ in range(CASE_NUMBERS)
    ]
    for t in range(2, 10):
        sort = shell_sort_factory(t)
        copyed_case = [a.copy() for a in cases]
        total_time = 0.0
        for case in copyed_case:
            watch = StopWatch()
            sort(case)
            total_time += watch.stop()
        print("Total time: %4.4f, when t=%d" % (total_time, t))


if __name__ == '__main__':
    # smoke_test(shell_sort_factory(2))
    main()
