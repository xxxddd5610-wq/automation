#任务：读取csv文件
'''
使用 csv 模块读取 cases.csv。
使用 csv.DictReader() 读取数据。
每条测试用例转换成一个字典。
将所有测试用例保存到 cases 列表中。
打印读取到的用例总数。
'''

import csv

def read_csv(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        cases = list(csv.DictReader(f))

        print(f"成功读取到测试用例：{len(cases)} 条")

read_csv("../data/cases.csv")




