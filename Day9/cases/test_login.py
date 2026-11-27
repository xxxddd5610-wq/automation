import pytest

from ..utils.yaml_util import read_yaml
from ...Day4.day4_assert_lib import check_status_code
from ...Day4.day4_assert_lib import check_field_exists
from ...Day4.day4_assert_lib import check_response_time

cases = read_yaml("login.yaml")

class TestLogin:
    #数据
    @pytest.mark.parametrize("case", cases, ids=[c['desc'] for c in cases])
    def test_login(self, login_api, case):

        #发请求
        result = login_api.login()

        #断言

        check_status_code(result.status, case['expect_status'])
