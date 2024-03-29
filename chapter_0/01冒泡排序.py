"""
冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
这个算法的名字由来是因为越小的元素会经由交换慢慢 "浮" 到数列的顶端（升序或降序排列），
就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名 "冒泡排序"。


算法原理：
    * 比较相邻的元素，如果第一个比第二个大，就交换他们两个。
    * 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    * 针对所有的元素重复以上的步骤，除了最后一个。
    * 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

"""


def bubble_sort(nums):
    for i in range(len(nums) -1):
        flag = True     # 每一趟置 flag 为 True
        for j in range(0,len(nums) - i -1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] =nums[j+1],nums[j]
                flag = True
        # flag 为 True 说明到这趟已经没有交换，提前跳出循环，提高算法效率
        if flag:
            break
    return nums


s = [3,44,28,5,25,36,2,87,5]
print(bubble_sort(s))


"""
# 冒泡排序
def selectionSort(arr):
    # 记录最小数的索引
    for i in range(len(arr) -1):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

"""