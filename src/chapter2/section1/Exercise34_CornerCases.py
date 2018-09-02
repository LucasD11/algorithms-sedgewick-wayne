#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 15:12:34
"""
Corner Cases
"""

import numpy as np


def corner_cases(length):
    yield np.sort(np.random.random(length))
    yield np.sort(np.random.random(length))[::-1]
    yield np.ones(length)
    yield np.random.randint(0, 1, length)


def selection_sort(a):
    for i in range(len(a)):
        min_j = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]


def shell_sort(a):
    h = 1
    while h < len(a) // 3:
        h = 3 * h + 1

    while h > 0:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] <= a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h = h // 3


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def main():
    for sort in [selection_sort, insertion_sort, shell_sort]:
        for case in corner_cases(1000):
            sort(case)
            assert (np.sort(case) == case).all()


if __name__ == '__main__':
    main()
