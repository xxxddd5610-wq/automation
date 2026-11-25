#题 1：把 "2026-11-25 08:00:00 INFO user login success" 拆出日期、日志级别、消息三段；
s = "2026-11-25 08:00:00 INFO user login success"
s_list = s.split(" ", 3)
print(f"日期：{s_list[0]}")
print(f"日志级别：{s_list[2]}")
print(f"消息：{s_list[3]}")

#题 2：给定 [("login","pass"),("pay","fail"),("login","fail"),("pay","pass")]，
# 用字典统计每个用例的 pass/fail 数；
cases = [("login","pass"),("pay","fail"),("login","fail"),("pay","pass")]
dict = {}
for case in cases:
    dict[case[1]] = dict.get(case[1], 0) + 1
for key, value in dict.items():
    print(f"{key}: {value}次")


#题 3：读可能不存在的 scores.txt（每行一个分数）求平均分，文件不存在时友好提示、不崩溃；
total = 0
try:
    with open("scores.txt", "r", encoding="utf-8") as f:

        num_list = f.readlines()
        for str_num in num_list:
            total += float(str_num)

except FileNotFoundError as e:
    print(e)
if total != 0:
    print(f"平均分为：{total/len(num_list):.2f}")