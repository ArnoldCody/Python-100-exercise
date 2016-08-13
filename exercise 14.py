# coding:utf-8
# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# import sys
def Prime_num(i):
    prime = False
    n = 2
    while i%n != 0 and n<i:
        n += 1
        while n == i:
            prime = True
            break
    return prime

def factor_analysis(i):
    factor = []
    if Prime_num(i):
        print "%d is a Prime Number, there is no factors" % i
    else:
        n=2
        print "%d =" % i, # 用，在同一行打印
        while n<i:
            if i%n == 0:
                i = i/n
                factor.append(n)
                # sys.stdout.write(str(n)) # 在同一行打印
                # sys.stdout.write("*")
                n = 2

            else:
                n+=1

        for n in factor:
            print "%d *" % n, # 用，在同一行打印
        print i


factor_analysis(231312)
