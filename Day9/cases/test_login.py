import pytest


from Day4.day4_assert_lib import check_status_code
from Day4.day4_assert_lib import check_field_exists
from Day4.day4_assert_lib import check_response_time
from Day4.day4_assert_lib import check_equal
from Day9.conftest import load_cases

cases = load_cases("login.yaml")

class TestLogin:
    #数据
    @pytest.mark.parametrize("case", cases, ids=[c['desc'] for c in cases])
    def test_login(self, login_api, case):

        #发请求
        result = login_api.login(case)
        print(result.text)

        #断言
        #http状态码
        check_status_code(result.status_code, case['expect_status'])

        res_json = result.json()

        #业务码
        check_equal(res_json['code'], case['expect_code'])

        #关键字段
        check_field_exists(res_json, "data")

        #响应时间
        response_time = result.elapsed.total_seconds()
        check_response_time(response_time, case['response_time'])

