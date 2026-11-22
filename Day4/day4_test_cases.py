#模拟接口测试，使用断言库验证接口响应

from day4_assert_lib import check_status_code
from day4_assert_lib import check_response_time
from day4_assert_lib import check_field_exists
from day4_assert_lib import check_equal

login_response = {
    "status_code": 200,
    "response_time": 1.25,
    "json": {
        "code": 200,
        "msg": "登录成功",
        "token": "abc123"
    }
}

check_status_code(login_response["status_code"], 200)
check_response_time(login_response["response_time"], 2)
check_field_exists(login_response["json"], "token")
check_equal(login_response["json"]["code"], 200)

login_fail_response = {
    "status_code": 500,
    "response_time": 2.56,
    "json": {
        "code": 500,
        "msg": "账号或密码错误"
    }
}

check_status_code(login_fail_response["status_code"], 200)
check_response_time(login_fail_response["response_time"], 2)
check_field_exists(login_fail_response["json"], "token")

register_response = {
    "status_code": 200,
    "response_time": 0.85,
    "json": {
        "code": 200,
        "msg": "注册成功",
        "user_id": 1001
    }
}

check_status_code(register_response["status_code"], 200)
check_response_time(register_response["json"]["code"], 200)
check_field_exists(register_response["json"], "user_id")