"""
1.6 打鱼还是晒网
1．问题描述
中国有句俗语叫“三天打鱼两天晒网”。某人从1990年1月1日起便开
始“三天打鱼两天晒网”，问这个人在以后的某一天中是“打鱼”还是“晒网”。
2．问题分析
根据题意可以将解题过程分为以下三步：
1）计算从1990年1月1日开始至指定日期共有多少天。
2）由于“打鱼”和“晒网”的周期为5天，所以将计算出的天数用5去
除。
3）根据余数判断他是在“打鱼”还是在“晒网”。
若余数为1，2，3，则他是在“打鱼”，否则是在“晒网”。
3．算法设计
本题目使用的算法为数值计算算法，要利用循环求出指定日期距
1990年1月1日的天数，并考虑到循环过程中的闰年情况，闰年二月为29
天，平年二月为28天。判断闰年的方法可以用伪语句描述如下：
如果能被4整除并且不能被100整除或者能被400整除，则该年是闰
年，否则不是闰年。
提示：在Python语言中判断能否整除可以使用求余运算符“%”。
4．确定程序框架

"""


# 判断是否为闰年，是：则返回1 ，否，则返回0
def runYear(year):
    if(year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):  # 是闰年
        return 1
    else:
        return 0


# 计算指定日期距离 1990年1月1日的天数
def countDay(currentDay):
    # 每月天数数组
    perMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    totalDay = 0
    year = 1990
    while year < currentDay['year']:    # 求出指定日期之前的每一年的天数之和
        if runYear(year) == 1:          # 判断是否为闰年
            totalDay = totalDay + 366
        else:
            totalDay = totalDay + 365
        year += 1

    # 如果是闰年，则二月份是 29 甜
    if runYear(currentDay['year'])==1:
        perMonth[2] += 1
    i = 0
    while i< currentDay['month']:
        totalDay += perMonth[i]     # 将本年内的天数累加到 totalDay 中
        i += 1

    totalDay += currentDay['day']   # 将本月内的天数累加到 totalDay 中

    return totalDay


if __name__=="__main__":
    while True:
        print("please input 指定日期 包括年,月,日 如:1999 1 31")
        year, month, day = [int(i) for i in input().split()]
        # 定义一个日期字典
        today = {'year': year, 'month': month, 'day': day}
        totalDay = countDay(today)  # 求出指定日期距离1990年1月1日的天数
        print("%d年%d月%d日与1990年1月1日相差 %d 天" % (year, month, day,totalDay))
        # 天数 % 5，判断输出打鱼还是晒网
        result = totalDay % 5
        if result > 0 and result < 4:
            print("今天打鱼")
        else:
            print("今天晒网")



"""
下面介绍字典的常用操作方法。
·dict.clear()：清空字典，也就是删除字典中的所有元素。
·dict.copy()：复制字典，返回一个具有相同键/值对的新字典，是浅复制。
·dict.fromkeys(seq[,value])：创建一个新字典，以序列seq中的元素作为字典的键，value为字典所有键对应的初始值。
·dict.get(key,default=None)：获取键key的value值，如果值不存在，就返回默认值。
·dict.items()：以列表的形式返回可遍历的（键/值）元组数组。
·dict.keys()：以列表的形式，返回字典中的所有键。
·dict.pop(key)：删除键key。
·dict.update(dict2)：更新字典元素，用于把字典dict2的键/值对更新到dict中。
·dict.values()：以列表的形式返回字典中的所有值。

"""






