#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 22:32:45
"""
Evalute Time Cost
"""
import time


class StopWatch:
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return time.time() - self.start


def evalute_time_cost(sort_function, array):
    watch = StopWatch()
    sort_function(array)
    return watch.stop()
