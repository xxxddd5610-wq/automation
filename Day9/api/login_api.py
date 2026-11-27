#登录请求
from Day9.api.base_api import BaseApi

class LoginApi(BaseApi):
    def login(self, case):

        data = {
            "account": case['account'],
            "password": case['password']
        }

        return self.post("/login/account", json=data)