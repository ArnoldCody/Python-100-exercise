# coding:utf-8
# 题目：暂停1s输出

"""
time.sleep(...)
        sleep(seconds)

        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
"""

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
	print key, value
	time.sleep(1) # 暂停 1 秒
