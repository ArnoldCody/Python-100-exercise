# coding:utf-8
"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222
(此时共有5个数相加)，几个数相加有键盘控制。
"""

n = raw_input("几个数字相加: ")
num = raw_input("每一位是几: ")
s = [0]
for i in range(1, n+1):
    s.append(num*10**(i-1)+s[i-1])
    if i < n:
        print s[i], "+",

print s[n], "=", sum(s)

print s
