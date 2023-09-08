"""

问题：给定一个M进制的数x，实现对x向任意一个非M进制的数的转换。

二进制、八进制、十进制、十六进制


第一类：0~9 间字符。0~127 之间字符型与整型是可以通用的，得到的差即为字符ch对应的数字。
第二类：A ~ Z 间字符

        int(x)：将其他类型转换成数字
        ord(x)：将字符转换成对应的 Unicode 码
        str(x)：将其他类型转换成字符串
        char(x)：将十进制数字转换成对应的字符

"""


# 将字符转换成数字
def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)
    else:
        return ord(ch)


# 将数字转换为字符
def num_to_char(num):
    if num >= 0 and num <= 9:
        return str(num)  # 将 0~9 之间的数字转换成字符
    else:
        return chr(num)  # 将大于10的数字转换成字符


# 其他数制转换成十进制
def source_to_decimal(temp, source):
    decimal_num = 0  # 存储展开之后的和

    for i in range(len(temp)):  # 累加
        decimal_num = (decimal_num * source) + char_to_num(temp[1])
    return decimal_num


# 十进制转换成其他数列
def decimal_to_object(decimal_num, object):
    decimal = []
    while decimal_num:
        # 求出余数并转换为字符
        decimal.append(num_to_char(decimal_num % object))
        decimal_num //= object
    return decimal


# 修改余数数制
def output(decimal):
    f = len(decimal) - 1
    while f >= 0:
        print(decimal[f], end='')
    f -= 1
    print()


if __name__=='__main__':
    MAXCHAR = 101       # 允许的最大字符串长度
    flag = 1            # 存储是否退出程序的标志
    while flag:         # 利用输入的flag值控制循环是否结束
        print("转换前的数是：", end='')
        temp = input()
        print("转换前的数制是：", end='')
        source = int(input())
        print("转换后的数制是：", end='')
        object = int(input())
        print("转换后的数是：", end='')
        decimal_num = source_to_decimal(temp, source)
        decimal = decimal_to_object(decimal_num, object)
        output(decimal)
        print("继续请输入1,否则输入0：")
        flag = int(input())

