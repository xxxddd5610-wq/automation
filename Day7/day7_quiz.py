#题 1：把 "2026-11-25 08:00:00 INFO user login success" 拆出日期、日志级别、消息三段；
s = "2026-11-25 08:00:00 INFO user login success"
s_list = s.split(" ", 3)
print(f"日期：{s_list[0]}")
print(f"日志级别：{s_list[2]}")
print(f"消息：{s_list[3]}")

#题 2：给定 [("login","pass"),("pay","fail"),("login","fail"),("pay","pass")]，
# 用字典统计每个用例的 pass/fail 数；


#题 3：读可能不存在的 scores.txt（每行一个分数）求平均分，文件不存在时友好提示、不崩溃；