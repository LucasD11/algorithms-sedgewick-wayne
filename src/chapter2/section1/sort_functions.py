#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 22:31:10
"""
Sort Algorithms
"""


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


def shell_sort(a):
    h = 1
    while h < len(a) // 3:
        h = 3 * h + 1
    while h > 0:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h = h // 3
