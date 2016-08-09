# coding: utf-8

"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""

# 程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

# 程序源代码：

"""
I = int(raw_input("Please input your profit > "))
branch_mark = [0, 100000, 200000, 400000, 600000, 1000000]
bonus_rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
bonus = []

for i in range(1,6):

    while (branch_mark[i-1] < I < branch_mark[i]) or (I >= branch_mark[i] >= 1000000):

        bonus.append((I - branch_mark[i-1]) * bonus_rate[i-1])

        while i>2:
            bonus.append((branch_mark[i-1] - branch_mark[i-2]) * bonus_rate[i-2])
            i = i-1

        break

print bonus
print sum(bonus)
"""

# better codes

I = int(raw_input("Please input your profit > "))
branch_mark = [1000000, 600000, 400000, 200000, 100000, 0]
bonus_rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = []

for i in range(0,6):
    while I > branch_mark[i]:
        bonus.append((I - branch_mark[i]) * bonus_rate[i])
        I = branch_mark[i] #利用 for 迭代的顺序，我觉得这个赋值很巧妙


print bonus
print sum(bonus)
