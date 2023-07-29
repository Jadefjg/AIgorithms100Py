"""
项目：二维数组，每行分别递增，每列分别递增，给定某些数字，判别是不是在此数组里面。采用面向对象的编程方式，接口自己定义，给出最优最快查找算法代码

"""


# 法1:
def find(self,target,array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if target == array[i][j]:
                return True
    return False



"""
法2：行列搜索

思想：按列按行搜索，由于二维数组的特殊特征，可规定由下到上，由左道右依次比较大小查找。
从二维数组的左下开始对比某数，若该数比目标的数值大，说目标数值应该为该数的右侧，则进行右移；
若该数比目标的数值小，说明目标数值应该为该数的上侧，则进行上移。
若整体搜索一遍后没有找到，说明搜索的数不存在。
"""


def find(target,array):
    row_count = len(array)
    i = 0
    colum_count = len(array[0])
    j = len(array[0]-1)
    while i <row_count and j >=0:
        value = array[i][j]
        if value == target:
            return True
        elif value > target:
            j -= 1
        else:
            i += 1
    return False


# 方法3：
def find_number(matrix, target):
    if not matrix or len(matrix[0]) == 0:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return False
