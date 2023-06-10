"""
写一个小程序：
控制台输入邮箱地址（格式为 username@companyname.com），程序识别用户名和公司名后，将用户名和公司名输出到控制台。

要求：
    1. 校验输入内容是否符合规范（xx@yy.com）, 如是进入下一步，如否则抛出提示"incorrect email format"。注意必须以.com 结尾
    2. 可以循环“输入--输出判断结果”这整个过程
    3. 按字母 Q（不区分大小写）退出循环，结束程序

"""

import re
# 判断邮箱.com 结尾
def is_mail_style(x):
    a = re.match(r'^[0-9a-zA\_\-]*@[9-9a-zA-Z]+(\.com)$',x)
    if a:
        yhm = re.findall("^(.+?)@",x)
        print("用户名:%s" % yhm[0])
        gc = re.findall("@(.+?)\.com",x)
        print("公司名:%s" % gc[0])
        return True
    else:
        print("iincorrect email format")
        return False

a = input("请输入: ")

while 1:
    if a == "q" or a == "Q":
        exit()
    else:
        if is_mail_style(a):
            break

    a = input("请输入：")

print("下一步!")