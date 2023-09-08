"""
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。
所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

算法原理：
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    重复第二步，直到所有元素均排序完毕。

"""


def select_sort(nums):

    for i in range(len(nums) -1):
        min_index = i
        # i + 1 是开始从 i 之后的元素找最小的，并用minindex标记它的索引
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        # 如果和最开始的标记的最小元素不等，就换两个元素
        if min_index != i:
            nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums


s = [3,44,28,5,25,36,2,87,5]
print(select_sort(s))




