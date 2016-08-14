# coding:utf-8

"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""
a = 3
b = 1
i = 1
for i in range(1, 4): # 打印前三行
    print " "*a, "*"*b, " "*a
    i += 1
    a = a-1
    b += 2
while i>=1: # 打印后四行
    print " "*a, "*"*b, " "*a
    i -= 1
    a = a+1
    b -= 2
