import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# 读取Excel文件
file_path = r'E:\素材2\资料\统计建模数据 (3)\千河公路桥WQI预测.xlsx'
data = pd.read_excel(file_path)

# 查看数据的列名和前几行，确认数据结构
print(data.columns)
print(data.head())

# 创建一个完整的时间列，从年、月、日、小时拼接
data['时间'] = pd.to_datetime(data[['年', '月', '日']].astype(str).agg('-'.join, axis=1) + ' ' + data['小时'].astype(str) + ':00', format='%Y-%m-%d %H:%M')

# 选择预测WQI-DET变量
wqi_det = data['预测WQI-DET'].dropna()

# Mann-Kendall趋势检测函数
def mann_kendall_test(data):
    n = len(data)
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s += np.sign(data[j] - data[i])

    var_s = n * (n - 1) * (2 * n + 5) / 18
    if s > 0:
        z = (s - 1) / np.sqrt(var_s)
    elif s < 0:
        z = (s + 1) / np.sqrt(var_s)
    else:
        z = 0
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value

# 对预测WQI-DET进行趋势检验
z_value, p_value = mann_kendall_test(wqi_det)
print(f'Mann-Kendall test results: Z = {z_value:.2f}, P = {p_value:.3f}')
