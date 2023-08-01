class Singleton:
    __instance = None

    def __new__(cls,age,name):
        # 如果类属性 __instance 值为None
        # 那么就创建一个对象，并且赋值为这个对下象引用，保证下次调用这个方法时
        # 能够知道之前已经创建过对象了，这样就保证了只有1个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


a = Singleton(18,"刚刚")
b = Singleton(10,'祖祖')

print(a)
print(b)
