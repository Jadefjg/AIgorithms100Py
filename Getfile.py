import os


def get_files(path='D:\\xx', rule=".py"):
    all = []
    for fpathe, dirs, fs in os.walk(path):  # os.walk 是获取所有的目录
        for f in fs:
            filename = os.path.join(fpathe, f)
            if filename.endswith(rule):  # 判断是否是"xxx"结尾
                all.append(filename)
    return all


if __name__ == "__main__":
    b = get_files(r"D:\PycharmPro\ZZot")
    for i in b:
        print(i)