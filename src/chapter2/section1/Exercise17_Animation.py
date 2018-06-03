#!/usr/bin/env python
# coding=utf-8
#
# Title: 2.1.17 Animation
# Author: Lucas
# Date: 2018-06-03 18:05:13
#
import time
import random
import matplotlib.pyplot as plt


LEN = 100


class Sort(object):
    def main(self):
        a = [random.random() for _ in range(LEN)]
        # Init plot lib
        plt.ion()
        self.show(a)
        self.sort(a)
        input("Press ENTER to close this program!")

    def exchange(self, a, i, j):
        a[i], a[j] = a[j], a[i]
        self.show(a)

    def show(self, a):
        plt.clf()
        plt.bar(range(len(a)), a, fc='r')
        plt.draw()
        plt.pause(0.01)

    @staticmethod
    def less(a, b):
        return a < b

    def sort(self, a):
        raise NotImplementedError


class Selection(Sort):
    def sort(self, a):
        for index in range(len(a)):
            min_index = index
            for j in range(index, len(a)):
                if self.less(a[j], a[min_index]):
                    min_index = j
            self.exchange(a, min_index, index)
        return a


class Insertion(Sort):
    def sort(self, a):
        for i in range(1, len(a)):
            for j in range(i, 0, -1):
                if self.less(a[j], a[j-1]):
                    self.exchange(a, j, j-1)
        return a



if __name__ == '__main__':
    Insertion().main()
