#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 22:01:55
"""
Various Types of Items
"""

import sys
import string

import numpy as np
import matplotlib.pyplot as plt

from sort_functions import insertion_sort, selection_sort, shell_sort
from evalute_time import evalute_time_cost


def generate_testcase1(length):
    """string"""
    return np.array(
        [''.join(np.random.choice(list(string.ascii_letters), size=10)) for _ in range(length)]
    )


def generate_testcase2(length):
    """
    Double
    """
    return np.random.random(length)


def generate_testcase3(length):
    """
    int
    """
    return np.random.randint(0, 100000, length)


def plot_time_graph(x, y, text=""):
    plt.plot(x, y)
    plt.xlabel("Array Length")
    plt.ylabel("Running Time")
    plt.title(text)


def main():
    sort_titles = zip(
        [selection_sort, insertion_sort, shell_sort],
        ['Selection', 'Insertion', 'Shell']
    )
    generator_titles = list(zip(
        [generate_testcase1, generate_testcase2, generate_testcase3],
        ["string", "double", "int"]
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
            plot_time_graph(lengths, total_times, text="%s-%s" % (title, g_title))
    plt.show()


if __name__ == '__main__':
    main()
