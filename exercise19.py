# coding:utf-8
# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

import exercise14

for n in range(0, 1000):
    if exercise14.perfect_numbe_analysis(n) == True:
        print "%d is a perfect number." % n
