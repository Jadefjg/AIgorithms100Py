"""
分糖果：
    10个小孩围成一圈分糖果，老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，
    ，第6个小孩4块，第7个小孩10块，第8个小孩6块，第9个小孩14块，第10个小孩20块。
    然后所有的小孩同时将手中的糖分一半给右边的小孩；糖块数为奇数的人可向老师要一块。
    问经过这样几次后大家手中的糖一样多？每人各有多少块糖？


"""


# 判断每个孩子手中的糖果数是否相同
def judge(candy):
    for i in range(0,10):
        if candy[0] != candy[i]:
            return 1 # 不相同返回1
    return 0 # 相同返回0


def giveSweets(sweet, j):
    t = [0] * 10
    while (judge(sweet)): # 若不满足要求则继续循环
        # 将每个孩子手中的糖果数平分为两份
        for i in range(0, 10):
            if sweet[i] % 2 == 0: # 若为偶数则直接分出一半
                sweet[i] = sweet[i] // 2
                t[i] = sweet[i]
            else:   # 若为奇数则加1后再分出一半
                sweet[i] = (sweet[i] + 1) // 2
                t[i] = sweet[i]
        # 将分出的一半糖果给右边的孩子
        for n in range(0, 9):
            sweet[n + 1] = sweet[n + 1] + t[n]
        sweet[0] += t[9]
        j += 1
        printResult(sweet, j)


# 输出列表中每个元素的值
def printResult(s,j):
    print("%4d" % j, end=" ")
    k = 0
    while k<10:
        print("%4d" % s[k], end=" ")
        k += 1
        j += 1
    print()


if __name__=="__main__":
    # 定义一个列表来存储老师给每个孩子分配的糖果数
    # sweet[0]=10表示第一个小孩的糖果数为10，以此类推
    sweet = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
    print("child 1 2 3 4 5 6 7 8 9 10")
    print("..........................................................")
    print("次数 糖果数")
    # 输出每个孩子手中的糖果数
    j = 0
    print("%4d" % j, end=" ")
    for i in range(len(sweet)):
        print("%4d" % sweet[i], end=" ")
    print()
    giveSweets(sweet, j)





