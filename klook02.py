"""

在排序数组中查找元素的第一个和最后一个位置

描述：给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target
要求：找出给定目标值在数组中的开始位置和结束位置。
说明：要求使用时间复杂度为 0(log n)的算法解决问题


"""


def searchRange(nums, target):
    def binarySearch(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    index = binarySearch(nums, target)
    if index == -1:
        return [-1, -1]

    start, end = index, index
    while start > 0 and nums[start - 1] == target:
        start -= 1
    while end < len(nums) - 1 and nums[end + 1] == target:
        end += 1

    return [start, end]

# 示例测试
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))  # 输出: [3, 4]

nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums, target))  # 输出: [-1, -1]




