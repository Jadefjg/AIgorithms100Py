"""
插入排序的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能懂。
插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入。

算法原理：
    * 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    * 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
     （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面）

"""

def insert_ort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] -= arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr


s = [3,44,28,5,25,36,2,87,5]
print(insert_ort(s))

