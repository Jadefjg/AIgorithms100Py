"""

归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。
该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：
    * 自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
    * 自下而上的迭代；

和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。

算法原理：
    开辟内存空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
    设定两个指针，最初位置分别为两个已经排序序列的起始位置；
    比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
    重复步骤 3 直到某一指针达到序列尾；
    将另一序列剩下的所有元素直接复制到合并序列尾。

"""

from math import floor


def merge_sort(arr):
    if (len(arr)<2):
        return arr

    # 二分
    middle = floor(len(arr)/2)
    left,right = arr[0:middle],arr[middle:]
    # 递归
    return merge(merge_sort(left),merge_sort(right))


def merge(left,right):
    result = []
    # 分治
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


s = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print(merge_sort(s))

