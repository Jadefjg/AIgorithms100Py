
class Student(object):
    __instance = None       # instance: 实例

    def __new__(cls,name,age,sex):
        # if not hasattr(cls,'__instance'):     # 判断是否有单例
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

hmh = Student('hmh',18,'male')
hhl = Student('hh1',18,'female')

print(hmh,hhl)
print(id(hmh),id(hhl))




