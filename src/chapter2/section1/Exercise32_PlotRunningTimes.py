#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-01 19:59:36
"""
Plot Running Times
------------------
"""

import argparse
import time

import numpy as np
import matplotlib.pyplot as plt


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


def smoke_test(sort):
    a = np.random.random(1000)
    sort(a)
    assert (np.sort(a) == a).all()


class StopWatch:
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def evalute_time_cost(sort, array_length, times):
    total_time = 0.0
    for _ in range(times):
        a = np.random.random(array_length)
        watch = StopWatch()
        sort(a)
        total_time += watch.stop()
    return total_time / times


def plot_time_graph(x, y, text=""):
    plt.plot(x, y, 'ro')
    plt.xlabel("Array Length")
    plt.ylabel("Case")
    plt.title("Algrothm %s Running Time" % text)
    plt.show()


def main():
    # CLI args and help text
    parser = argparse.ArgumentParser(
        description="Plot Running Times for different sorting algorithms"
    )
    parser.add_argument(
        "algorithm",
        type=str,
        choices=["insertion", "selection", "shellsort"],
    )
    parser.add_argument(
        "-l",
        "--length",
        dest="length",
        type=int,
        default=1000,
        help="Length of array need to be sort"
    )
    parser.add_argument(
        "-t",
        dest="times",
        type=int,
        default=20,
        help="Number of running times for this array length"
    )
    args = parser.parse_args()

    if args.algorithm == 'selection':
        sort = selection_sort
    elif args.algorithm == 'insertion':
        sort = insertion_sort
    elif args.algorithm == 'shellsort':
        sort = shell_sort
    else:
        raise Exception("Unsupported Sort Algorithm")

    # Run sort algorithm
    total_time = []
    for _ in range(args.times):
        total_time.append(evalute_time_cost(sort, args.length, 1))

    # Draw graph
    plot_time_graph(range(args.times), total_time)


if __name__ == '__main__':
    # smoke_test(selection_sort)
    # smoke_test(insertion_sort)
    # smoke_test(shell_sort)
    main()
