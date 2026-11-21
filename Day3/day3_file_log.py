#day3：文件操作练习

#任务1：生成模拟日志
'''
你是一名软件测试工程师，现在需要分析某个系统的接口访问日志。
系统每天会产生大量访问记录，你需要通过 Python 程序完成以下工作：
1. 自动生成模拟访问日志 mock_access.log。
2. 读取日志，统计不同 HTTP 状态码出现的次数。
3. 筛选出所有 5xx 服务器错误日志，写入 errors.log。
4. 将状态码统计结果保存到 result.csv。
5. 如果日志文件不存在，需要进行异常处理，不能让程序直接崩溃。
'''

import random
import csv
from datetime import datetime, timedelta

def generate_mock_file(log_file, total_line):
    method = ["GET", "POST"]
    code = [200, 301, 400, 401, 501, 502]
    path = ["/api/login", "/api/register", "/api/user", "/api/order", "/api/list"]

    start_time = datetime(2026, 11, 21, 15, 0, 0)
    current_time = start_time

    with open(log_file, "w", encoding="utf-8") as f:
        for _ in range(total_line):
            m = random.choice(method)
            c = random.choice(code)
            p = random.choice(path)

            time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")

            line = f"{time_str} {m} {p} {c}\n"
            f.write(line)

            current_time = current_time + timedelta(seconds=3)
    print(f"写入完毕，文件名:{log_file}")

generate_mock_file("mock_access.log", 100)

#任务2:读取日志并统计状态码
'''
读取 mock_access.log 文件，统计不同 HTTP 状态码出现的次数。
要求：
1. 使用 open() 打开文件。
2. 使用 with open() 管理文件。
3. 使用 readlines() 或逐行读取的方式获取日志。
4. 使用字典保存状态码及对应次数。
5. 遍历字典，打印统计结果。
'''

def read_mock_file(log_file, csv_file):
    code_dict = {}

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip().split()
                code = line_list[-1]

                code_dict[code] = code_dict.get(code, 0) + 1

        print("=====HTTP状态码统计=====")

        for key, value in code_dict.items():
            print(f"{key}: {value}次")

        print("====================")

    except FileNotFoundError as e:
        print(f"文件{log_file}没有找到，请检查文件路径")
        print(e)
        return

        # 任务2：csv
        #这里newline是为了防止一行数据一行空白行
    with open(csv_file, "w", encoding="utf-8", newline = '') as f2:
        writer = csv.writer(f2)
        writer.writerow(["status_code", "count"])

        for key, value in code_dict.items():
            writer.writerow([key, value])
    print(f"已将统计状态码结果写入{csv_file}")


read_mock_file("mock_access.log", "result.csv")

#任务3：提取5XX错误日志
'''
在读取日志的基础上，筛选所有 HTTP 状态码为 5xx 的记录，并保存到 errors.log。
要求：
1. 只提取 500、502 两种状态码。
2. 使用循环逐行判断。
3. 将符合条件的完整日志写入 errors.log。
4. 不要只写入状态码，需要保留整行日志。
5. 最终打印提取出的错误日志数量。
'''

def generate_error_log(orign_file, log_file):

    error_count = 0

    with open(orign_file, "r", encoding = "utf-8") as f1:
        with open(log_file, "w", encoding = "utf-8") as f2:
            for line in f1:
                line_list = line.strip().split()
                code = line_list[-1]

                if code == "501" or code == "502":
                    error_count += 1
                    f2.write(line)

    print("=====5XX错误日志提取=====")
    print(f"发现服务器错误日志：{error_count}条")
    print(f"已成功写入{log_file}")
    print("====================")

generate_error_log("mock_access.log", "errors.log")

#任务4：统计结果写入CSV
'''
将任务2中得到的状态码统计结果保存到 result.csv。
要求：
1. 使用 Python 内置 csv 模块。
2. 第一行为表头：status_code,count。
3. 后续每一行保存一个状态码及对应数量。
4. CSV 文件必须能够正常使用 Excel 打开。
'''

#已合并到任务2里

#任务5：异常处理
'''
给日志文件读取操作增加异常处理。
要求：
1. 使用 try-except。
2. 捕获 FileNotFoundError。
3. 当 mock_access.log 不存在时，打印友好的错误提示。
4. 不允许程序直接输出一大段异常堆栈信息。
5. 文件存在时，正常执行后续统计操作
模拟场景：先将 mock_access.log 重命名为 mock_access_backup.log，再运行程序。
'''

def except_exercise(test_file):
    try:
        with open(test_file, "r", encoding="utf-8") as f:
            for line in f:
                print(line)

    except FileNotFoundError as e:
        print(f"错误：未找到{test_file}文件，请检查文件路径！")
        print(e)

except_exercise("hiad.txt")