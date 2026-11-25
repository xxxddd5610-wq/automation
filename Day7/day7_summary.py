#扫描 automation/ 目录下所有 *_report.txt / *_report.csv（Day 5、Day 6 的产物），
# 汇总本周累计：总用例数、通过数、失败数、通过率，终端打印并写入 week1_summary.txt；
#知识点pathlib

from pathlib import Path
import csv

#这里路径..是当前工作目录的上一级工作目录
base_dir = Path("..")
patterns = ["*_report.txt", "*_report.csv"]
reports = []
for p in patterns:
    reports.extend(base_dir.rglob(p))

pass_count = 0
fail_count = 0
case_count = 0

print(reports)

for file in reports:

    if file.suffix == ".csv":
        try:
            with open(file, "r", encoding="utf-8-sig") as f:
                cases = csv.DictReader(f)
                for case in cases:
                    if case['result'] == "PASS":
                        pass_count += 1
                    else:
                        fail_count += 1
                    case_count += 1
        except FileNotFoundError as e:
            print(e)

    if file.suffix == ".txt":
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in file:
                    if not line:
                        continue
                    line = line.strip()
                    if "PASS" in line:
                        pass_count += 1
                        case_count += 1
                    else:
                        fail_count += 1
                        case_count += 1

        except FileNotFoundError as e:
            print(e)

if reports:
    print(f"总用例数: {case_count}")
    print(f"通过数：{pass_count}")
    print(f"失败数：{fail_count}")
    print(f"通过率：{pass_count/case_count * 100:.2f}%")
