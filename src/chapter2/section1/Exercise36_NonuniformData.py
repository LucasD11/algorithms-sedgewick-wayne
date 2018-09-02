#!/usr/bin/env python
# coding=utf-8
#
# Author: Lucas (yuanzhendai@gmail.com)
# Date: 2018-09-02 19:12:48
"""
Nonuniform Data
"""

import numpy as np


def generate_nonuniform_testcase1(length):
    return np.random.randint(0, 1, size=length)


def generate_nonuniform_testcase2(length):
    return np.random.geometric(p=0.5, size=length)


def generate_nonuniform_testcase3(length):
    result = []
    for _ in range(length):
        if np.random.random() > 0.5:
            result.append(0)
        else:
            result.append(np.random.randint(1, 10000))
    return np.array(result)
