#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:00:11 2017

@author: meng
"""

import random;
unsortData = random.sample(range(100), 10)

def insertion_sort(lst):
    if len(lst) == 1:
        return lst

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

print ("Original Data:", unsortData)
sortData = insertion_sort(unsortData);
print ("Sorted Data:", sortData)