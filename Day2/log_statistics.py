#小练习1：模拟日志success/fail词频统计
#业务场景：你正在进行接口自动化测试，需要分析一段接口运行日志，统计接口请求成功和失败次数

logs = """
login success
register success
login fail
create_form success
login success
delete_form fail
register success
login fail
create_form success
login success
"""

result_count = {}

logs = logs.strip()
list_logs = logs.split('\n')
print(list_logs)

for i in list_logs:
    tmp_list = i.split()
    result_count[tmp_list[1]] = result_count.get(tmp_list[1], 0) + 1

all_count = 0
for key, value in result_count.items():
    all_count += value
    print(f"{key}: {value}")

print(f"总请求数：", all_count)
if all_count > 0:
    #这里要规避没有success键和除数为0的情况
    rate = round(result_count.get("success", 0)/all_count * 100, 2)
    print(f"成功率：{rate}%")

