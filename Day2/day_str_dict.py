#一、基础练习：字符串与字典基础练习
#题目1：接口响应数据数据处理
response = "  login_success,register_success,login_fail,login_success  "

response = response.strip()

list_res = response.split(",")

#注意遍历的对象
for i in range(len(list_res)):
    list_res[i] = list_res[i][0].upper() + list_res[i][1:]

print(list_res)

#题目2：接口测试结果统计
test_results = {
    "test_login": "PASS",
    "test_register": "FAIL",
    "test_create_form": "PASS",
    "test_delete_form": "PASS",
    "test_update_form": "FAIL",
    "test_query_form": "PASS"
}

pass_count = 0
fail_count = 0

for key, value in test_results.items():
    if value == "PASS":
        pass_count += 1
    if value == "FAIL":
        fail_count += 1

    print(f"{key}: {value}")

print(f"通过数量：{pass_count}")
print(f"失败数量：{fail_count}")