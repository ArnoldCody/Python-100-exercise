# coding:utf-8
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。再由大到小输出

num = []
for i in range(3):
    x = int(raw_input("please input a number: "))
    num.append(x)

num.sort()
print num
num.sort(reverse=True)
print num
