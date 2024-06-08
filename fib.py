# def fib(n):
#     a,b = 0,1
#     while a < n:
#         print(a,end=' ')
#         a,b  = b, a+b
#     print()
#
# fib(10)


# def fib2(n):
#     """return a list containing the Fibonacci series up to n."""
#     result = []
#     a,b = 0,1
#     while a < n:
#         result.append(a)
#         a,b = b,a+b
#     return result
#
# print(fib2(100))


def fib3(n):
    if n <= 1:
        return n
    else:
        return fib3(n-1) + fib3(n-2)

# n_terms = 10
# if n_terms <= 0:
#     print("请输入一个正整数")
# else:
#     print("斐波拉契函数")
#     for i in range(n_terms):
#         print(fib3(i))


def main(n_terms):
    if n_terms <= 0:
        print("请输入一个正整数")
    else:
        print("斐波拉契函数")
        for i in range(n_terms):
            print(fib3(i))


if __name__=="__main__":
    main(10)



