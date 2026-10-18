import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置中文和负号正确显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的意思
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV文件
file_path = r'E:\素材2\资料\统计建模数据 (3)\高家川.csv'  # 替换为正确的文件路径
data = pd.read_csv(file_path,encoding='gbk')
data['监测时间'] = pd.to_datetime(data['监测时间'], errors='coerce')
numeric_cols_with_time = data.select_dtypes(include=[np.number, 'datetime'])
filtered_weekly_data = numeric_cols_with_time.resample('W', on='监测时间').mean()

# Mann-Kendall趋势检测函数
def mann_kendall_test(data):
    n = len(data)
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s += np.sign(data[j] - data[i])
    var_s = n * (n - 1) * (2 * n + 5) / 18
    z = s / np.sqrt(var_s) if s != 0 else 0
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value

# 绘图函数
def plot_data_with_trends(column_name):
    y = filtered_weekly_data[column_name].dropna()
    x = np.arange(len(y))
    slope, intercept = np.polyfit(x, y, 1)
    trend_line = slope * x + intercept
    trend_equation = f"y = {slope:.2f}x + {intercept:.2f}"
    z_value, p_value = mann_kendall_test(y)
    trend_details = f"Z: {z_value:.2f}, P: {p_value:.3f}"

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(y.index, y, color='skyblue')
    ax.plot(y.index, trend_line, color='red', linestyle='--', label='趋势线')
    ax.set_xlabel('潼关吊桥传统公式WQI')
    ax.set_ylabel('I值')
    ax.legend(loc='upper left')
    ax.annotate(f"{trend_equation}\n{trend_details}", xy=(0.95, 0.95), xycoords='axes fraction', fontsize=12,
                horizontalalignment='right', verticalalignment='top',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="b", lw=2))

    # 在图中添加水平线和标签
    levels = [1.0, 2.0, 3.0, 4.0, 5.0]
    labels = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ']
    for level, label in zip(levels, labels):
        ax.axhline(y=level, color='black', linestyle='--', linewidth=1)
        ax.text(1.02, level, label, va='center', ha='left', transform=ax.get_yaxis_transform())

    plt.tight_layout()
    plt.show()

# 调用绘图函数
column_to_plot = 'WQI-DET'  # 指定要绘制的列名
plot_data_with_trends(column_to_plot)
