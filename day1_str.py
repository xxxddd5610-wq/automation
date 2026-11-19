#练习字符串
'''
练习 3（25min）· 字符串：
给定字符串 "2026-11-19 08:43:27 ERROR login failed"，
用字符串方法切出日期、级别（ERROR）和消息三部分，分别打印。
'''
s = "2026-11-19 08:43:27 ERROR login failed"

result = s.split(" ", 3)

date = result[0]
level = result[2]
message = result[3]

print("日期：", date)
print("级别：", level)
print("消息：", message)


#接口响应数据清理（去除首尾空格并打印）
s = "  login_success  "
s = s.strip()
print(s)

#日志内容替换（将admin替换为test, 将123456替换为******）
s = "user admin login failed, password=123456"
s = s.replace("admin", "test")
s = s.replace("123456", "******")
print(s)

'''
组合练习，去除字符串首尾空格，提取日期，提取日志级别，提取日志消息。
将消息中的admin替换为test，分别打印日期、级别和消息
'''
s = "  2026-11-19 09:30:16 ERROR user admin login failed  "

s = s.strip()
result = s.split(" ", 3)

date = result[0]
level = result[2]
message = result[3].replace("admin", "test")

print("日期：", date)
print("级别：", level)
print("消息：", message)