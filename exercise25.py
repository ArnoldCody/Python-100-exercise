# coding:utf-8
"""
题目：求1+2!+3!+...+20!的和。
"""
import math

s = 0
for i in range(1,21):
    s += math.factorial(i)

print s
