#
# def binary_search(alist,keys):
#
#     if keys not in alist:
#         print(str(keys) + "不在数组里面")
#         return -1
#
#     n = len(alist)
#
#     if n == 0:
#         return False
#
#     mid = n // 2
#
#     if alist[mid] > keys:
#         return binary_search(alist[:mid], keys)
#     elif alist[mid] < keys:
#         return binary_search(alist[mid+1:],keys)
#     elif alist[mid] == keys:
#         print(str(keys) + "在数组里面的第" + str(mid) + "个位置")
#         return alist[mid]
#
#
# if __name__=='__main__':
#     array = [-1,0,3,5,9,12]
#     keys = 9
#     print(binary_search(array,keys))


# def binary_search(arrs, keys):
#
#     min = 0                 # 最低位
#     max = len(arrs) - 1     # 最高位
#
#     if keys in arrs:
#         while True:        # 建立一个死循环，直到找到key
#             mid = (min + max) // 2      # 中位数
#             if arrs[mid] > keys:         # key在数组左边
#                 max = mid - 1
#             elif arrs[mid] < keys:       # key在数组右边
#                 min = mid + 1
#             elif arrs[mid] == keys:       # key在数组中间
#                 print(str(keys) + "在数组里面的第" + str(mid) + "个位置")
#                 return arrs[mid]
#     else:
#
#         print("该数字" + str(keys) + "不存在！")
#         return -1
#
#
# if __name__ == "__main__":
#     arrys = [-1,0,3,5,9,12]
#     key = 9
#     binary_search(arrys, key)


# def binary_search(nums, keys):
#     min = 0                 # 最低位
#     max = len(nums) - 1     # 最高位
#
#     while min <= max:
#         mid = (min + max) // 2      # 中位数
#         if nums[mid] == keys:
#             return mid
#         elif nums[min] <= keys < nums[mid]:
#             max = mid - 1
#         else:
#             min = mid + 1
#
#     return -1
#
#
# if __name__=='__main__':
#     array = [-1,0,3,5,9,12]
#     keys = 0
#     print(binary_search(array,keys))


def binary_search(num, n):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid = (left + right) // 2

        if num[mid] == n:
            return mid

        if num[left] <= num[mid]:  # 判断左一半是不是升序的

            if num[left] <= n < num[mid]:  # 如果是升序的话 判断目标是否在 left mid 里面
                right = mid - 1  # 在里面的话更新 right
            else:  # 虽然是升序 但目标不在这里面
                left = mid + 1  # 更新 left 直接舍去这部分

        else:  # 右一半是升序的

            if num[mid] < n <= num[right]:  # 判断目标是否在 mid right 里面
                left = mid + 1  # 在里面更新 left
            else:  # 目标不在这里面 更新 right
                right = mid - 1

    return -1


if __name__=='__main__':
    array = [-1,0,3,5,9,12]
    keys = 9
    print(binary_search(array,keys))


