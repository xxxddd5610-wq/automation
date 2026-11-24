#任务1：读取csv文件
'''
使用 csv 模块读取 cases.csv。
使用 csv.DictReader() 读取数据。
每条测试用例转换成一个字典。
将所有测试用例保存到 cases 列表中。
打印读取到的用例总数。
'''

import csv

with open("../data/cases.csv", "r", encoding="utf-8") as f:
    cases = list(csv.DictReader(f))

    print(f"成功读取到测试用例：{len(cases)} 条")


#任务2：模拟接口响应数据
'''
根据传入的测试用例，返回一个模拟响应字典。
正常情况下返回与预期值一致的响应。
故意让 case_003、case_006、case_008 返回错误数据。
其他用例返回正确数据。
'''
def mock_response(case):
    if case['case_id'] == "case_003" or case['case_id'] == "case_006" or case['case_id'] == "case_008":
        response = {
            "status" : 200,
            "field": "success"
        }
    else:
        response = {
            "status" : case['expect_status'],
            "field": case['expect_field']
        }
    return response

#任务3：逐条执行测试用例
'''
1. 调用 mock_response() 获取实际响应。
2. 调用 Day4 中封装好的断言函数。
3. 校验实际状态码是否等于预期状态码。
4. 校验实际字段是否等于预期字段。
5. 断言成功，返回 PASS。
6. 断言失败，返回 FAIL。
'''

from Day4.day4_assert_lib import check_status_code
from Day4.day4_assert_lib import check_field_exists
def run_case(case):

    res = mock_response(case)

    try:
        check_status_code(res['status'], case['expect_status'])
        check_field_exists(res['field'], case['expect_field'])
        return "PASS"
    except AssertionError:
        return "FAIL"





