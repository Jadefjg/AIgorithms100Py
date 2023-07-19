import re


def expand_string(input_str):
    # pattern = r'(\w+)\[([^\[\]]+)\](\w+)'
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    match = re.search(pattern, input_str)

    if match:
        x = match.group(1)
        options = match.group(2).split("|")
        y = match.group(3)

        return [x + option + y for option in options]
    else:
        return [input_str]


# input_str = "x[a|b]y"
input_str = "诗云科技的[下午茶|夜宵][好吃|难吃]死了"
result = expand_string(input_str)
print(result)  # 输出：['xay', 'xby']