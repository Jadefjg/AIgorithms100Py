class A(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance


a = A()
print(a)



#
# 资源共享：日志、应用配置
# 资源控制：网站计数器、应用配置、多线程池、数据库配置、应用程序日志



