# python实现：x[a|b]y=>[xay,xby]

# import re
#
#
# def expand_string(input_str):
#     pattern = r'(\w+)\[([^\[\]]+)\](\w+)'
#     match = re.search(pattern, input_str)
#
#     if match:
#         x = match.group(1)
#         options = match.group(2).split("|")
#         y = match.group(3)
#
#         return [x + option + y for option in options]
#     else:
#         return [input_str]
#
#
# def main():
#     str = "诗云科技的[下午茶|夜宵][好吃|难吃]死了"
#     print(expand_string(str))
#     str = "[上|这|下]道题有点[难|简单]"
#     print(expand_string(str))
#
#
# if __name__=="__main__":
#     main()


import re


def expand_string(input_str):
    pattern = r'(\w+)\[([^\[\]]+)\](\w+)'
    match = re.search(pattern, input_str)

    if match:
        x = match.group(1)
        options = match.group(2).split("|")
        y = match.group(3)

        return [x + option + y for option in options]
    else:
        return [input_str]


input_str = "x[a|b]y"
result = expand_string(input_str)
print(result)  # 输出：['xay', 'xby']


# str1 = "k:1|k1:2|k2:3|k3:4"

# def str2dict(str1):
#     dict1 = {}
#     for iterms in str1.split('|'):
#         key,value = iterms.split(':')
#         # return key,value
#         dict1[key] = value
#     return dict1


# print(str2dict(str1).items())
# print(sorted(str2dict(str1).items(),key=lambda x:x[1]))

