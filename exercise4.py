# coding:utf-8
# 题目：输入某年某月某日，判断这一天是这一年的第几天？

birthday = raw_input("please input birthday, like yyyymmdd: ")

# 检验是否为闰年
def leap_year(year):
    if year%4 == 0:
        return True
    else:
        return False

# 定义每月的天数
def month_has_days(month):
    for i in [1, 3, 5, 7, 9, 10, 12]:
        if month == i:
            days = 31
    for i in [4, 6, 8, 11]:
        if month == i:
            days = 30
    if month == 2:
        if leap_year:
            days = 28
        else:
            days = 29
    return days

# 提取年月日
year = int(birthday[0:4])
day = int(birthday[6:8])
month = int(birthday[4:6])

# 检验输入日期是否正确
while month<1 or month>12 or day<1 or day>31:
    print "error"
    birthday = raw_input("please input birthday, like yyyymmdd: ")
    year = int(birthday[0:4])
    day = int(birthday[6:8])
    month = int(birthday[4:6])

# 计算天数
days = day
while month > 1:
    month = month - 1
    days += month_has_days(month)
    # print days

print "your birhtday is the %dth day in year %d." %(days, year)
