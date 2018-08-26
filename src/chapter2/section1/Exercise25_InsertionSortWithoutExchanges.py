#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas
# Date: 2018-08-27 00:28:30
"""
Insertion Sort without Exchanges
"""

import random

from Exercise24_InsertionSortWithSentinel import sort_compare, smoke_test_sort


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


def insertion_sort_without_exchange(a):
    for i in range(1, len(a)):
        last = a[i]
        j = i
        while j > 0 and a[j-1] > last:
            a[j] = a[j-1]
            j -= 1
        a[j] = last


if __name__ == '__main__':
    smoke_test_sort(insertion_sort)
    smoke_test_sort(insertion_sort_without_exchange)
    sort_compare(insertion_sort, insertion_sort_without_exchange, 1000, 100)
