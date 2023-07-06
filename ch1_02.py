
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

# 兔子总数规律 类似于斐波拉契函数
a = 0
b = 1
while b < 100:
    print(b, end=",")
    a, b = b, a+b

    print(a,b)




