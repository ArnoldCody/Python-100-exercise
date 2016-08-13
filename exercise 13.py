# coding:utf-8

"""
题目：打印出所有的"水仙花数"（Narcissistic number），所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
"""

for i in range(100, 1000):
    units = i / 100
    tnes = i / 10 % 10
    hundreds = i % 10
    if units**3 + tnes**3 + hundreds**3 == i:
        print i
