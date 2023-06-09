"""
1.2 兔子产子
1．问题描述
有一对兔子，从出生后的第3个月起每个月都生一对兔子。小兔子长到第3个月后每个月又生一对兔子，假设所有的兔子都不死，问30个月内每个月的兔子总对数为多少？

2．问题分析
兔子产子问题是一个有趣的古典数学问题，我们画一张表来找一下兔子数的规律，如表1.1所示。
说明：不满1个月的兔子为小兔子，满1个月不满2个月的为中兔子，满3个月以上的为老兔子。

可以看出，每个月的兔子总数依次为1，1，2，3，5，8，13…这就是Fibonacci数列。总结数列规律即为从前两个月的兔子对数可以推出第3个月的兔子对数。

3．算法设计
本题目是典型的迭代循环，即是一个不断用新值取代变量的旧值，然后由变量旧值递推出变量新值的过程。这种迭代与这些因素有关：
初值、迭代公式和迭代次数。经过问题分析，算法可以描述为

用Python语言来描述迭代公式即为fib=fib1+fib2，其中fib为当前新求出的兔子对数，fib1为前一个月的兔子对数，fib2为前两个月的兔子
对数，然后为下一次迭代做准备， ，进行如下的赋值 fib2=fib1，fib1=fib，要注意赋值的次序；迭代次数由循环变量控制，为所求的月数。

4. 完整的程序

"""
# 方法1：
# if __name__=="__main__":
#     fib1 = 1    # 代表前一个月的数量
#     fib2 = 2
#     i = 3
#     print("%6d   %6d" % (fib1,fib2),end="   ")
#     while i<=30:
#         fib = fib1 + fib2
#         print("%6d" % fib, end=" ")
#         if i % 4 == 0:
#             print()
#         fib2 = fib1
#         fib1 = fib
#         i += 1


"""
6．问题拓展
这个程序虽然是正确的，但可以进行改进。目前用3个变量来求下一个月的兔子对数，其实可以在循环体中一次求出下两个月的兔子对数，这样就可以只用两个变量来实现。这里将fib1+fib2的结果不放在fib
中而是放在fib1中，此时fib1不再代表前一个月的兔子对数，而是代表最新一个月的兔子对数，再执行fib2=fib1+fib2，由于此时fib1中已经是第3个月的兔子对数了，故fib2中就是第4个月的兔子对数。可以看出，
此时fib1和fib2均为最近两个月的兔子对数，循环推出下两个月的兔子对数。改进后的程序如下：
"""
# 方法2：

if __name__=="__main__":
    fib1 = 1    # 最新一个月的兔子对数
    fib2 = 1
    i = 1
    while i<=15:    # 每次求两个，因此循环遍历循环到 15
        print("%8d   %8d" % (fib1, fib2), end="   ")
        fib = fib1 + fib2
        if i % 2 == 0:
            print()
        fib1 = fib1 + fib2  # 最新一个月的兔子对数
        fib2 = fib1 + fib2  # 第4个月的兔子对数
        i += 1


