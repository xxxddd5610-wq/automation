#验证接口响应速度

import requests

from Day4.day4_assert_lib import check_response_time

url = "http://192.168.182.188:8999/user/form/create"

headers = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY3MiIsImlhdCI6MTc5NTUxMDMxNSwiZXhwIjoxNzk2MTE1MTE1fQ.D62A4BF4JyV24h1_gGHx7Wmt0fkAtrLg6KCh9MEc6q7d8EiDUKTotX7pe_WK2DdqlDuZbq2Fsh5X2ly12EG6lw"
}

data = {
    "description": "",
    "name": "时间校验",
    "type": 0,
    "folderId": 0
}

response = requests.post(url, headers=headers, json=data, timeout=5)

res_time = response.elapsed.total_seconds()

try:
    check_response_time(res_time, 0.08)
    print(f"验证通过，响应时间小于0.08")
except AssertionError as e:
    print(e)