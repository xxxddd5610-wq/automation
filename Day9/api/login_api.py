#登录请求
from utils.yaml_util import read_yaml
from base_api import BaseApi


class LoginApi(BaseApi):
    def login(self):

        path = "../config/config.yaml"

        data_dic = read_yaml(path)

        data = {
            "account": data_dic['account'],
            "password": data_dic['password']
        }

        return self.post("/login/account", json=data)