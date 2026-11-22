#题目1：封装HTTP状态码断言
'''
判断实际状态码是否等于预期状态码。
相等则正常通过，不做额外处理。
不相等则抛出 AssertionError。
错误信息必须包含实际状态码和预期状态码。
'''

def check_status_code(actual, expected):
        assert actual == expected, (
            f"状态码校验失败, 预期状态码：{expected}, 实际状态码：{actual}"
        )

#题目2：封装接口响应时间断言
'''
登录接口的响应时间不能超过 2 秒。
要求：
1. 实际响应时间小于等于预期时间，验证通过。
2. 实际响应时间超过预期时间，抛出 AssertionError。
3. 错误信息包含实际耗时和最大允许耗时。
4. 响应时间保留两位小数展示。
'''
def check_response_time(actual, expected):
        assert actual <= expected, (
            f"接口响应时间超限, 实际耗时：{actual:.2f}, 允许最大耗时：{expected:.2f}"
        )

#题目3：封装响应字段存在性断言
'''
判断指定字段是否存在。
存在则验证通过。
不存在则抛出 AssertionError。
错误信息包含缺失的字段名称。
'''

def check_field_exists(response, field):
    assert field in response, (
        f"字段存在性校验失败, 字段{field}不存在"
    )

#题目4：封装实际值与预期值比较断言
'''
判断实际值与预期值是否相等。
相等则验证通过。
不相等则抛出 AssertionError。
错误信息必须显示实际值和预期值。
'''
def check_equal(actual, expected):
        assert actual == expected, (
            f"字段值校验失败, 实际结果为：{actual}, 预期结果为：{expected}"
        )