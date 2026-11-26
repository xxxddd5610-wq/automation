#GET请求练习：
'''
测试目标：验证GET请求参数传递是否正确
输入:
"timestamp": "1795678815410",
"sign": "4b67a64b1a7e3a123dd34626d760cb97"

预计输出：
HTTP 状态码为200
响应 字段data存在
响应 data.current = 1
'''
import requests

from Day4.day4_assert_lib import check_status_code
from Day4.day4_assert_lib import check_field_exists
from Day4.day4_assert_lib import check_equal

url = "http://192.168.182.188:8999/user/form/page"

headers = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTY3MiIsImlhdCI6MTc5NTUxMDMxNSwiZXhwIjoxNzk2MTE1MTE1fQ.D62A4BF4JyV24h1_gGHx7Wmt0fkAtrLg6KCh9MEc6q7d8EiDUKTotX7pe_WK2DdqlDuZbq2Fsh5X2ly12EG6lw"
}

params = {
    "timestamp": "1795678815410",
    "sign": "4b67a64b1a7e3a123dd34626d760cb97"
}

response = requests.get(url, headers=headers, params=params, timeout=5)

#状态码是否相同
try:
    check_status_code(response.status_code, 200)
    print(f"HTTP 状态码为: {response.status_code}")
except AssertionError as e:
    print(e)

res_json = response.json()

#字段是否存在
try:
    check_field_exists(res_json, "data")
    print(f"字段值data存在")
except AssertionError as e:
    print(e)

try:
    check_equal(res_json['data']['current'], 1)
    print(f"data.current = {res_json['data']['current']}")
except AssertionError as e:
    print(e)



