# coding:utf-8
"""
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
list = []
a, b = 2.0, 1.0
list.append(a/b)
i = 1
while i < 20:
    i += 1
    a, b = a+b, a
    list.append(a/b)
    
print sum(list)
