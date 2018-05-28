#!/usr/bin/env python
# coding=utf-8
#
# Title: 2.1.12 Shellsort count compares
# Author: Lucas
# Date: 2018-05-28 23:30:34
#
import random


class ShellSortCompares(object):
    def __init__(self):
        self.count = 0

    def less(self, i, j):
        self.count += 1
        return i < j

    def exchange(self, a, i, j):
        a[i], a[j] = a[j], a[i]

    def sort(self, a):
        h = 1
        while h < len(a) // 3:
            h = 3 * h + 1

        while h >= 1:
            for i in range(h, len(a)):
                for j in range(i, h-1, -h):
                    if self.less(a[j], a[j-h]):
                        self.exchange(a, j, j-h)
                    else:
                        break
            h = h // 3

        return a

    def is_sorted(self, a):
        for i, j in zip(a, sorted(a)):
            if i != j:
                return False
        return True

    def main(self, a):
        a = self.sort(a)
        if not self.is_sorted(a):
            raise Exception(' '.join([str(i) for i in a]))

        return a, self.count


if __name__ == '__main__':
    n = 100
    while n < 100000000000:
        # case = [5, 3, 1, 4, 2, 4, 3, 2, 1, 4]
        case = [random.random() for _ in range(n)]
        _, count = ShellSortCompares().main(case)
        print("n:%d   compares:%d" % (n, count))
        n = n * 10

