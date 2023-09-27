"""
爱因斯坦的数学题：
    爱因斯坦出了一道这样的数学题：
    有一条长阶梯，若每步跨2阶，则最后剩一阶，若每步跨3阶，则最后剩2阶，若每步跨5阶，则最后剩4阶，若每步跨6阶，则最后剩5阶。
    只有每次跨7阶，最后才正好一阶不剩。请问在1到n内，有多少个数能满足？


"""


def computing_ladder(n):
    print("在 1-%d 之间的阶梯数为：" %n)
    sum = 0
    for i in range(7,n+1):
        # 阶梯数所满足的条件
        if (i % 7 == 0) and (i % 6 == 5) and (i % 5 == 4) and (i % 3 == 2):
            sum += 1        # sum 记录 1~n 之间满足条件的阶梯个数
            print("%d" % i)
    print("在 1-%d之间,有%d个数可以满足爱因斯坦 对阶梯的要求。" % (n,sum))


if __name__=="__main__":
    while True:
        n = int(input("请输入 n 值："))
        computing_ladder(n)
