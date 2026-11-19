'''
练习 1（20min）· 列表：
写一个脚本，定义一个列表 codes = [200, 404, 200, 500, 200, 403]，
统计 200 出现的次数，并把去重后的状态码按从小到大打印。
预期输出：200 出现 3 次 和 [200, 403, 404, 500]。
'''
codes = [200, 404, 200, 500, 200, 403]
count = 0
for index, value in enumerate(codes):
    if value == 200:
        count += 1

print(f"200出现{count}次，{list(set(codes))}")
