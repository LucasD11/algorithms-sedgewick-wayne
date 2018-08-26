#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-26 18:01:11
"""
Selection Sort
"""


def selection_sort(a):
    for i in range(len(a)):
        i_min = i
        for j in range(i+1, len(a)):
            if a[j] < a[i_min]:
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]
    return a


def smoke_test():
    import random
    a = [random.randint(0, 10000) for _ in range(1000)]
    assert sorted(a) == selection_sort(a)
    print(a[:100])


if __name__ == '__main__':
    smoke_test()
