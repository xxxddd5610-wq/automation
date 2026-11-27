#封装登录的requests

import requests

class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        self.session.headers.updata({"token": token})

    def post(self, path, json=None):
        return self.session.post(self.base_url + path, json=json, timeout=10)

    def get(self, path, params=None):
        return self.session.get(self.base_url + path, params=params, timeout=10)



