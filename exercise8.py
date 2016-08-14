# coding:utf-8
# 题目：输出9*9乘法口诀表。

for i in range (1,10):
    for n in range (1, i+1):
        print "%d 乘以 %d 等于 %d" % (n, i, i*n)
    print " "
