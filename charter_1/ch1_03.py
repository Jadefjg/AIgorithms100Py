

# 函数功能是用牛顿迭代法求方程的根
def solution(a,b,c,d):
    x = 1.5
    x0 = x      # 用所求得的 x 的值代替 x0 原来的值
    # f 用来描述方程的值，fd用来描述方程求导之后的值
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 + 2 * b * x0 + c
    h = f / fd
    x = x0 - h      # 求得更接近方程根的 X 值
    while abs(x - x0) >= 1e-5:
        x0  = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 + 2 * b * x0 + c
        h = f / fd
        x = x0 - h      # 求得更接近方程根的 x 值
    return x


if __name__=="__main__":
    print("请输入方程的系数:")
    # a,b,c,d 代表所求方程的系数
    a,b,c,d = map(float,input().split())
    print("方程的参数为：",a,b,c,d)
    # x 用来记录求得的方程根
    x = solution(a,b,c,d)
    print("所求方程的根为 x=%.6f"%x)












