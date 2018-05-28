#!/usr/bin/env python
# coding=utf-8
#
# Title: 2.1.11 Shellsort with incrementSequence saved
# Author: Lucas
# Date: 2018-05-28 23:07:19
#
class ShellSort(object):
    def is_sorted(self, a):
        sorted_a = sorted(a)
        for i, j in zip(a, sorted_a):
            if i != j:
                return False
        return True

    def sort(self, a):
        increment_sequence = [1]
        while increment_sequence[-1] < len(a) // 3:
            increment_sequence.append(increment_sequence[-1] * 3 + 1)

        for h in increment_sequence:
            for i in range(h, len(a)):
                for j in range(i, h-1, -h):
                    if a[j] >= a[j-h]:
                        break
                    a[j], a[j-h] = a[j-h], a[j]
        return a

    def main(self, a):
        a = self.sort(a)
        if not self.is_sorted(a):
            raise Exception
        return a


if __name__ == '__main__':
    case = [4, 3, 2, 1, 5]
    print(ShellSort().main(case))
