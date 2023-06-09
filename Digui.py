# 问题1：计算 n!

"""
方法1:可以用 python 里面的 reduce 函数，reduce() 函数会对参数序列中元素进行累积

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用
传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
from functools import reduce

a = 10

# b = reduce(lambda x,y: x*y, range(1,a+1))
#
# print(b)


# 法2：不用 lambda ，写个函数
def chengfa(x,y):
    return x*y

b = reduce(chengfa,range(1,a+1))

print(b)


# 方法3
def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)
print(digui(a))


# 方法4：用 for 循环(不推荐)
a = 10
s = 1
for i in range(1,a+1):
    s = s*i
    print(s)




