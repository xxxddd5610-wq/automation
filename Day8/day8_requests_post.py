#POST练习
'''
使用 requests.post() 发送请求。
通过 json 参数传递请求数据。
通过 headers 参数传递自定义请求头。
获取响应 JSON。
使用 Day 4 的断言函数完成校验。
'''

import requests

from Day4.day4_assert_lib import check_equal
from Day4.day4_assert_lib import check_status_code
from Day4.day4_assert_lib import check_field_exists

url = "http://192.168.182.188:8999/user/form/create"

headers = {
    "Content-Type": "application/json",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY3MiIsImlhdCI6MTc5NTUxMDMxNSwiZXhwIjoxNzk2MTE1MTE1fQ.D62A4BF4JyV24h1_gGHx7Wmt0fkAtrLg6KCh9MEc6q7d8EiDUKTotX7pe_WK2DdqlDuZbq2Fsh5X2ly12EG6lw"
}

data = {
    "description": "",
    "name": "pytest测试",
    "type": 0,
    "folderId": 0
}

response = requests.post(url, headers= headers, json=data, timeout=5)


try:
    check_status_code(response.status_code, 200)
    print(f"HTTP实际值：{response.status_code}")
except AssertionError as e:
    print(e)

res_json = response.json()

try:
    check_field_exists(res_json, "data")
    print(f"字段data存在")
except AssertionError as e:
    print(e)


try:
    check_equal(res_json['data']['deleted'], False)
    print(f"字段data.deleted为{res_json['data']['deleted']}")
except (AssertionError, KeyError) as e:
    print(e)