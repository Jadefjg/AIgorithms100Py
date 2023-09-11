# """
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
#
# 示例 1：输入：x = 121 输出：true
#
# 示例 2：输入：x = -121 输出：false 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
# 示例 3：输入：x = 10 输出：false 解释：从右向左读, 为 01 。因此它不是一个回文数。
#
# 示例 4：输入：x = -101 输出：false
#
# 采用python语言进行编写
# 可以采用字符串的切片等方法对输入的数据进行处理我们可以知道字符串的 [index] 索引方法，[-1]是从字符串的最后一个元素向前索引。
# 我们可以编写得到如下代码：
# """
#
# figure = int(input('请输入一个数字： '))
# Str = str(figure)
# l = len(Str)//2   #利用整除得到需要比较的次数
# k = 0
# for i in range(l):
#     if Str[i] != Str[-1-i]:
#         break  #判断出不是回文数时直接跳出循环
#     k += 1
#
# if k == l:
#     print(figure, '是回数 ')
# else:
#     print(figure, '不是回数 ')
#



# 法2
# def huixie():
#     num = input('请输入要判断是否为回文数的数：')
#     if (num[::-1] == num[:]):
#
#         print('%s为回文数'%num)
#     else:
#         print('%s不是回文数'%num )
# huixie()
#
# 法3
# ent=input("请输入一句话: ")
# a=ent[0::1]
# b=ent[-1::-1]
# if a==b:
#     print("回数")
# else:
#     print("不是回数")

list=input("请输入一句话: ")
print(type(list))
print(list[0::1])
print(list[-2::-1])




