# def fib(n):
#     a,b = 0,1
#     while a < n:
#         print(a,end=' ')
#         a,b  = b, a+b
#     print()
#
# fib(10)


def fib2(n):
    """return a list containing the Fibonacci series up to n."""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

print(fib2(100))




