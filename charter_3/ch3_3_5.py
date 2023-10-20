"""

亲密数：

1．问题描述
    如果整数A的全部因子（包括1，不包括A本身）之和等于B，且整数B的全部因子（包括1，不包括B本身）之和等于A，则将整数A和B称为亲密数。
    求3000以内的全部亲密数。


2．问题分析
    按照亲密数定义，要判断整数a是否有亲密数，只要计算出a的全部因子的累加和，将其存到变量b，再计算b的全部因子的累加和设为n，
    若n等于a，则可判定a和b是亲密数。


3．算法设计
    计算数a的各因子的算法：用a依次对i（i的范围可以是1～a-1或1～a/2-1）进行模（“%”，
    在编程过程中一定要注意求模符号两边参加运算的数据必须为整数）运算，若结果等于0，则i为a的一个因子；否则i就不是a的因子。
    将所求得的因子累加到变量b。接下来求变量b的因子：算法同上，将b的因子之和累加到变量n。根据亲密数的定义判断变量n是否等于变量a（if(n==a)），
    若相等，则a和b是一对亲密数，反之则不是。


"""
if __name__=="__main__":
    print("3000以内的全部亲密数为：")
    for a in range(1, 300): # 穷举3000以内的全部整数
        b = 0
        i = 1
        while i <= (a//2): # 计算数 a 的各因子，将各因子之和存放到b中
            if a % i == 0:
                b += i
        i += 1

    n = 0 # 计算b的各因子，将各因子之和存于 n
    j = 1
    while j <= (b//2):
        if b % j == 0:
            n += j
        j += 1

    if n == a and a < b:
        print("%4d -- %4d \t" %(a, b))


# if __name__=="__main__":
#     print("3000以内的全部亲密数为：")
#     b = 0
#     n = 0
#     for a in range(3000): # 穷举30000以内的全部整数
#         # 计算数a的各因子，将各因子之和存放到b中
#         i = 1
#         while i <= (a//2):
#             if a % i == 0:
#                 b += i
#         i += 1
#
#     # 计算b的各因子，将各因子之和存于n
#     j = 1
#     while j <= (b//2):
#         if b % j == 0:
#             n += j
#         j += 1
#
#     if n == a and a < b:
#         print("%4d -- %4d \t" %(a, b))



