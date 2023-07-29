"""

存在重复元素

描述：给定一个整数数组，nums
要求：判断是否存在重复的元素。如果有元素的数字钟出现至少两次，返回 True;否则返回 False
说明：1<= nums.length <= 10(5)
     -10(9) <= nums[i] <= 10(9)

"""


def func(nums):
    n_set = set()
    for num in nums:
        if num in n_set:
            return True
        n_set.add(num)
    return False


if __name__=="__main__":
    num1 = [1,2,3,1]
    print(func(num1))
    num2 = [1, 2, 3, 4]
    print(func(num2))


# def containsDuplicate(nums):
#     num_set = set()
#     for num in nums:
#         if num in num_set:
#             return True
#         num_set.add(num)
#     return False
#
# # 示例测试
# nums1 = [1, 2, 3, 1]
# print(containsDuplicate(nums1))  # 输出: True
#
# nums2 = [1, 2, 3, 4]
# print(containsDuplicate(nums2))  # 输出: False
