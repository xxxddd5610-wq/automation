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

#任务4：异常捕获，保证单条失败不中断
'''
1. 遍历所有测试用例。
2. 每条用例执行时使用 try/except。
3. 如果断言失败，捕获 AssertionError。
4. 将当前用例记录为 FAIL。
5. 继续执行下一条用例。
6. 所有用例执行完毕后，输出测试结果汇总。
'''

def run_all_cases(cases):
    results = []
    pass_count = 0
    fail_count = 0

    for case in cases:
        errors = []

        res = mock_response(case)

        try:
            check_status_code(res['status'], case['expect_status'])
        except AssertionError as e:
            errors.append(str(e))

        try:
            check_field_exists(res['field'], case['expect_field'])
        except AssertionError as e:
            errors.append(str(e))


        if not errors:
            result = "PASS"
            pass_count += 1
        else:
            result = "FAIL"
            fail_count += 1

        results.append({
            "case_id": case['case_id'],
            "case_name": case['name'],
            "expect_status": case['expect_status'],
            "actual_status": res['status'],
            "expect_field": case['expect_field'],
            "actual_field": res['field'],
            "result": result,
            "error_msg": ";".join(errors)
        })

    print("=====测试执行结果=====")
    for i in results:
        print(f"{i['case_id']} | {i['case_name']} | {i['result']}")
    print("===================")

    print("=====执行汇总=====")
    print(f"总用例数：{len(cases)}")
    print(f"通过数量：{pass_count}")
    print(f"失败数量：{fail_count}")
    print(f"通过率：{pass_count/len(cases) * 100:.0f}%")

    return results

#任务5：生成csv测试报告
'''
1. 使用 csv.DictWriter() 写入。
2. 使用 writeheader() 写入表头。
3. 使用 writerow() 或 writerows() 写入测试结果。
4. 失败用例需要记录具体失败原因。
5. 成功用例的 error_msg 可以为空。
'''
results = run_all_cases(cases)
with open("day6_report.csv", "w", encoding="utf-8", newline = "") as f:
    fieldnames = ["case_id", "case_name", "expect_status", "actual_status", "expect_field", "actual_field", "result", "error_msg"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for result in results:
        writer.writerow(result)
    print("执行情况已写入文件")







