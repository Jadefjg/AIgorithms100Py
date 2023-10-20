
"""
U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×arr[n-1] × (1÷arr[n]) if n is odd
U = arr[1]×arr[2]×(1÷arr[3])×arr[4]×...×(1÷arr[n-1]) × arr[n] if n is even
"""


# def max_Uodd(arr):
#     arr.sort(reverse=True)  # 将数组从大到小排序
#     if len(arr) % 2 != 0:   # 数组长度是否为奇数
#         arr[-1], arr[-2] = arr[-2], arr[-1]     # 倒数第一数与倒数第二数互换
#     count = 1
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             count *= arr[i]
#         else:
#             count *= 1 / arr[i]
#     return count
#
#
# if __name__=="__main__":
#     # 示例测试
#     arr= [5, 3, 2, 4, 1]
#     result = max_Uodd(arr)
#     print(result)  # 输出：7.5


def rearrange_array(arr):
    positive_integers = sorted([x for x in arr if x > 0])
    non_positive_integers = sorted([x for x in arr if x <= 0])

    non_positive_integers.reverse()

    merged_array = non_positive_integers + positive_integers

    if len(merged_array) % 2 != 0:
        last_element = merged_array.pop()
        merged_array.append(last_element)

    return merged_array


# 示例用法
arr = [4, -2, 0, 1, 5, -3]
rearranged_arr = rearrange_array(arr)
print(rearranged_arr)