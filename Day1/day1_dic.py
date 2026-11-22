#练习字典
'''
练习 2（25min）· 字典：
定义一个字典模拟接口响应 {"code": 0, "msg": "success", "data": {"username": "yaoling", "role": "tester"}}，
打印出 username 的值；再往字典里加一个键 "token": "abc123" 并打印整个字典。
'''
dic = {
    "code": 0,
    "msg": "success",
    "data": {
        "username": "yaoling",
        "role": "tester"
    }
}
print(dic["data"]["username"])
dic["token"] = "abc123"
print(dic)