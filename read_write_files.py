with open('example.txt', 'w') as file:
    file.write("这是一个写入文件的例子。\n欢迎学习Python!")

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)