#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-27 23:32:06
"""
Equal Keys
----------

If there are just 2 key values,

For selection sort: There will be O(n^2 / 2) compares and n exchanges.
For insertion sort: There will be O(n^2 / 4) compares and (n^2 / 4) exchanges.
"""

import random


class Item(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __repr__(self):
        return "<%d>" % self.value


def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            exchange(a, j, j-1)
            j -= 1


def selection_sort(a):
    for i in range(len(a)):
        min_j = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_j]:
                min_j = j
        exchange(a, i, min_j)


def smoke_test(sort):
    a = [Item(random.randint(0, 1)) for _ in range(1000)]
    sort(a)
    assert sorted(a, key=lambda x: x.value) == a
    # print(a[:100])


if __name__ == '__main__':
    smoke_test(insertion_sort)
    smoke_test(selection_sort)
