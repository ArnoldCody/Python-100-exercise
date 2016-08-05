# coding: utf-8
# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

num = [1, 2, 3, 4]
result = []

for n_100 in num:
    for n_10 in num:
        for n_1 in num:
            if (n_100 != n_10) and (n_10 != n_1) and (n_1 != n_100):
                result.append(int(n_100)*100 + int(n_10)*10 + int(n_1)*1)

print "There is total %d numbers" % len(result)
print result[0:]
