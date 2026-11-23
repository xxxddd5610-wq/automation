#编写迷你测试执行器，自动执行所有测试用例
from Day4.day4_assert_lib import check_equal
from Day4.day4_assert_lib import check_status_code

cases = [
    {
        "case_id": "case_001",
        "case_name": "正常登录",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 200,
        "expected_code": 200
    },
    {
        "case_id": "case_002",
        "case_name": "密码错误",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_003",
        "case_name": "账号为空",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_004",
        "case_name": "账号不存在",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_005",
        "case_name": "服务器异常",
        "actual_status": 500,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_006",
        "case_name": "正常注册",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 200,
        "expected_code": 200
    },
    {
        "case_id": "case_007",
        "case_name": "重复注册",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_008",
        "case_name": "参数缺失",
        "actual_status": 200,
        "expected_status": 200,
        "actual_code": 500,
        "expected_code": 500
    },
    {
        "case_id": "case_009",
        "case_name": "Token失效",
        "actual_status": 401,
        "expected_status": 401,
        "actual_code": 401,
        "expected_code": 401
    },
    {
        "case_id": "case_010",
        "case_name": "权限不足",
        "actual_status": 403,
        "expected_status": 200,
        "actual_code": 403,
        "expected_code": 200
    }
]

#任务1：实现单组用例执行
'''
遍历全部 10 组测试用例。
每组用例使用 try/except 进行异常隔离。
某组用例失败，继续执行下一组。
记录每组执行结果。
统计总用例数、通过数、失败数。
'''
def run_all(cases):

    results = []

    for case in cases:
        errors = []


        try:
            check_status_code(case["actual_status"], case["expected_status"])
            status_result = "PASS"
        except AssertionError as e:
            status_result = "FAIL"
            errors.append(str(e))

        try:
            check_equal(case["actual_code"], case["expected_code"])
            code_result = "PASS"
        except AssertionError as e:
            code_result = "FAIL"
            errors.append(str(e))

        if not errors:
            result = "PASS"
        else:
            result = "FAIL"

        results.append({
            "case_id": case["case_id"],
            "case_name": case["case_name"],
            "status_result": status_result,
            "code_result": code_result,
            "result": result,
            "reason": ";".join(errors)

        })

    pass_count = 0
    fail_count = 0

    print(f"=====用例执行明细=====")
    for i in results:
        if i['result'] == "PASS":
            pass_count += 1
        else:
            fail_count += 1
        print(f"{i['case_id']} | {i['case_name']} | {i['result']}")
        if i['result'] == "FAIL":
            print(f"{i['reason']}")

    print("=====接口自动化测试报告=====")
    print(f"执行总数：{len(cases)}")
    print(f"通过数量：{pass_count}")
    print(f"失败数量：{fail_count}")
    print(f"通过率：{pass_count/len(cases) * 100}%")


run_all(cases)

