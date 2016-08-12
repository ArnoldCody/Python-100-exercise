# coding=utf-8
"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""

"""
# 这个函数可以输出制定从 0~i 的数列，不叫省内存，计算 i 很大的时候很快得出结果
def Fib(i):
    Fib = []
    Fib.append(0)
    Fib.append(1)

    n = 2
    while n <= i:
        Fib.append(Fib[n-1]+Fib[n-2])
        n += 1

    return Fib[i-1]

i = int(raw_input("input a number: "))
print "the %dth number in Fibonacci sequence is %d." % (i, Fib(i))
"""
# 更简单的函数，但只能输出制定位置的菲波那切数，但是很占用内存
def Fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return Fib(i-2) + Fib(i-1)

i = int(raw_input("input a number: "))-1
print "the %dth number in Fibonacci sequence is %d." % (i+1, Fib(i))
