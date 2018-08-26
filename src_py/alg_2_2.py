#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-26 18:06:39
"""
Insertion Sort
"""


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
    return a


def smoke_test():
    import random
    a = [random.randint(0, 10000) for _ in range(1000)]
    assert sorted(a) == insertion_sort(a)


if __name__ == '__main__':
    smoke_test()
