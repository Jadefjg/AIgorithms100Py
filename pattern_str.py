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