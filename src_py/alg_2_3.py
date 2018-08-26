#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-26 18:21:31
"""
Shell Sort
"""


def shell_sort(a):
    h = 1
    while h < len(a) // 3:
        h = 3 * h + 1

    while h >= 1:
        # h-sort the array
        for i in range(h, len(a)):
            j = i
            while j > 0 and a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                j -= 1
        h = h // 3


def smoke_test():
    import random
    import copy
    a = [random.randint(0, 10000) for _ in range(1000)]
    a_copy = copy.copy(a)
    shell_sort(a)
    print(a[:100])
    assert sorted(a_copy) == a


if __name__ == '__main__':
    smoke_test()
