#小练习2：编写check_status_code断言函数
#业务场景：在接口自动化测试中，我们需要判断接口实际返回的HTTP状态码是否符合预期

def check_status_code(actual_code, expected_code):
    try:
        assert actual_code == expected_code, (
            f"实际状态码：{actual_code}, 预期状态码：{expected_code}"
        )
        print("PASS")
        return True
    except AssertionError as e:
        print("测试结果：FAIL")
        print(e)
        return False


check_status_code(200, 200)
check_status_code(400, 400)
check_status_code(500, 401)