# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 03:17:10 2021

@author: HI
"""

a=65
for i in range(6):
    for j in range(1, i+1):
        print("%c" %(a), end="")
        a += 1
    print()
