# coding:utf-8
# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import re
string = "13213109*(*!(*@    asdfwirejfiow))"

# 利用正则表达式匹配
def count(string):
    # 统计空格的字数
    num_space = string.count(" ")

    # 统计数字
    num_dig = len(re.sub(r'\D', "", string)) # 匹配所有非数字并删掉，保留所有数字

    # 统计字母
    num_word = len(re.sub(r'[^a-zA-Z]', "", string)) # 匹配所有非字母并删掉，保留所有字母

    # 统计其他字符
    num_other = len(re.sub(r'[a-zA-Z0-9]', "", string)) \
              - num_space # 匹配所有字母数字，并删掉，保留特殊字符，然后删掉空格
    print "there are %d spaces, %d digits, %d wrods, and "\
          "%d other comments in the sentence" % \
          (num_space, num_dig, num_word, num_other)

count(string)

# 利用 string 内置函数
"""
import string
s = raw_input('input a string:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print 'char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others)
"""
