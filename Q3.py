
stacklist = []


def stack_push(v):
    stacklist.append(v)


def stack_pop():
    if len(stacklist):
        v = stacklist.pop(-1)
    else:
        print('stacklist is empty !')
    return v


def inci(v,i):
    if len(stacklist) < i:
        return "堆栈元素数量不足"
    for j in range(i):
        stacklist[j] += v


if __name__=="__main__":
    v = 30
    i = 12
    print(stack_push(v))
    print(stack_pop())
    print(inci(v,i))



# 你可以使用 Python 中的列表来实现一个堆栈，并根据命令进行相应的操作。下面是一个示例的代码实现：

#
# stacklist = []
#
#
# def push(v):
#     stacklist.append(v)
#
#
# def pop():
#     if not stacklist:
#         return "堆栈为空"
#     return stacklist.pop()
#
#
# def inci(v, i):
#     if len(stacklist) < i:
#         return "堆栈元素数量不足"
#     for j in range(i):
#         stacklist[j] += v
#
#
# while True:
#     command = input("请输入命令：")
#     if command.startswith("push"):
#         v = int(command.split()[1])
#         push(v)
#     elif command == "pop":
#         print(pop())
#     elif command.startswith("inci"):
#         v, i = map(int, command.split()[1:])
#         print(inci(v, i))
#     else:
#         break
#
# if __name__=="__main__":
#     print(stacklist[-1] if stacklist else "堆栈为空")


# command = input("请输入命令：")
# print(command.split()[1])


# 法3
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        if self.is_empty():
            return 'EMPTY'
        else:
            return self.stack.pop()

    def inc(self, i, v):
        if not self.is_empty() and i > 0:
            for j in range(min(i, len(self.stack))):
                self.stack[j] += v

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if self.is_empty():
            return 'EMPTY'
        else:
            return self.stack[-1]


def stack_operations(operations):
    s = Stack()
    for op in operations:
        if op.startswith('push'):
            v = int(op.split()[1])
            s.push(v)
        elif op == 'pop':
            s.pop()
        elif op.startswith('inc'):
            i, v = map(int, op.split()[1:])
            s.inc(i, v)
        print(s.top())

# 示例用法
operations = ['push 5', 'pop', 'push 10', 'inc 2 5']
stack_operations(operations)