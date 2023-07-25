"""
项目：在二维数组中，每个元素中有一个整数，表示图形在该元素处的高度。需要计算出从左上角到右下角的最小路径和，每次可以向下或向右移动。

解析：给定一个二维数组中的每个元素表示一个格子的高度，任务就是找到从矩阵的左上角(0,0)到右下角(n-1，n-1)的最小路径和。
在每一步，你只能向下或向右移动。

"""

# 例如：给定以下 grid：
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]


def mp(grid):

    if not grid:
        return 0

    m,n = len(grid),len(grid[0])
    dp = [[0]*n for _ in range(m)]

    dp[0][0] = grid[0][0]

    # 初始化第一行
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    # 初始化第一列
    for j in range(1,m):
        dp[j][0] = dp[j-1][0] + grid[j][0]

    # 动态规划求解最小路径和
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]


if __name__=="__main__":
    print(mp(grid))