#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 22:01:55
"""
Partially Sorted
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

from sort_functions import insertion_sort, selection_sort, shell_sort
from evalute_time import evalute_time_cost


def generate_testcase1(length):
    """95% of return array is sorted, last 5% is random"""
    sorted_length = int(length * 0.95)
    a = np.sort(np.random.random(sorted_length))
    return np.concatenate((a, np.random.random(length - sorted_length)), axis=None)


def generate_testcase2(length):
    """
    All entries within 10 positions of their final place
    """
    return np.array([
        np.random.randint(10 * i-100, 10 * i+100) for i in range(length)
    ])


def generate_testcase3(length):
    """5% randomly put into a sorted array"""
    sorted_length = int(length * 0.95)
    a_sorted = np.sort(np.random.random(sorted_length))
    a_random = np.random.random(length - sorted_length)
    result = []
    i_sorted = 0
    i_random = 0
    for _ in range(length):
        if (np.random.random() > 0.05 or i_random >= len(a_random)) and i_sorted < len(a_sorted):
            result.append(a_sorted[i_sorted])
            i_sorted += 1
        else:
            result.append(a_random[i_random])
            i_random += 1
    return np.array(result)


def plot_time_graph(x, y, text=""):
    plt.plot(x, y)
    plt.xlabel("Array Length")
    plt.ylabel("Running Time")
    plt.title(text)


def main():
    sort_titles = zip(
        [selection_sort, insertion_sort, shell_sort],
        ['Selection Sort', 'Insertion Sort', 'Shell Sort']
    )
    generator_titles = list(zip(
        [generate_testcase1, generate_testcase2, generate_testcase3],
        ["5% Last Random", "Almost Sorted", "Random 5% Sorted"]
    ))
    plt.figure(1)
    for x, (sort, title) in enumerate(sort_titles):
        for y, (generator, g_title) in enumerate(generator_titles):
            print("\nGenerating Graph for %s %s" % (title, g_title))
            total_times = []
            lengths = []
            for length in range(200, 2000, 200):
                sys.stdout.write('*')
                sys.stdout.flush()
                for _ in range(10):
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    total_time = 0.0
                    total_time += evalute_time_cost(sort, generator(length))
                total_time = total_time / 10
                total_times.append(total_time)
                lengths.append(length)
            # Draw Graph
            print("Subplot %d done" % (1 + 3 * x + y))
            plt.subplot(3, 3, 1 + 3 * x + y)
            plot_time_graph(lengths, total_times, text="%s %s" % (title, g_title))
    plt.show()


if __name__ == '__main__':
    main()
