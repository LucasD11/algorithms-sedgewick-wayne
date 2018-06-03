#!/usr/bin/env python
# coding=utf-8
#
# Title: 2.1.16 Certification
# Author: Lucas
# Date: 2018-06-03 13:19:47
#
import random


class InternalSort(object):
    def sort(self, a):
        return sorted(a)

    @staticmethod
    def _elements_counts(origin):
        counts = {}
        for elem in origin:
            if elem in counts:
                counts[elem] += 1
            else:
                counts[elem] = 1
        return counts

    @staticmethod
    def _counts_equal(counts1, counts2):
        if len(counts1.keys()) != len(counts2.keys()):
            return False
        for key in counts1.keys():
            if key not in counts2 or counts1[key] != counts2[key]:
                return False
        return True

    def check(self, origin):
        counts_before = self._elements_counts(origin)
        sorted_list = self.sort(origin)
        counts_after = self._elements_counts(sorted_list)
        return self._counts_equal(counts_before, counts_after)


if __name__ == '__main__':
    case = [random.randint(0, 100) for _ in range(10000)]
    print(InternalSort().check(case))
