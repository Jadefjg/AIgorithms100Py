'''
问题: 三色球
    一个口袋中放有12个球，已知其中3个是红的，3个是白的，6个是黑的，现从中任取8个，问共有多少种可能的颜色搭配？
    从 12个球中任取8个，红球m个，白球n个，黑球 8-m-n个。m取值范围[0,3],n的取值范围[0,3]，黑球的个数小于等于8.即 8-m-n<=6
'''


def ball_type():
    print("\t 红球 \t 白球 \t 黑球")
    num = 0
    for m in range(0,4):
        for n in range(0,4):
            if 8-m-n <= 6:
                num += 1
                print("%2d: %d \t\t %d \t\t %d" % (num, m, n, 8 - m - n))


if __name__=='__main__':
    ball_type()
