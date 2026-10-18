# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import norm
#
# # 设置中文和负号正确显示
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的意思
# plt.rcParams['axes.unicode_minus'] = False
#
# # 读取CSV文件
# file_path = 'E:\\素材2\\资料\\新丰镇大桥_筛选数据.csv'  # 替换为正确的文件路径
# data = pd.read_csv(file_path, encoding='GBK')  # 或尝试 'GBK'
# print(data.columns.tolist())  # 输出所有列名
#
#
# # 确保监测时间列不被排除
# data['监测时间'] = pd.to_datetime(data['监测时间'], errors='coerce')
#
# # 选择包含数值和时间列的数据
# numeric_cols_with_time = data.select_dtypes(include=[np.number, 'datetime'])
#
# # 使用监测时间列进行重采样，计算每月的平均值
# filtered_monthly_data = numeric_cols_with_time.resample('W', on='监测时间').mean()
# filtered_monthly_data = filtered_monthly_data[filtered_monthly_data.index >= "2021-01-01"]
#
# # Mann-Kendall趋势检测函数
# def mann_kendall_test(data):
#     n = len(data)
#     s = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             s += np.sign(data[j] - data[i])
#
#     var_s = n * (n - 1) * (2 * n + 5) / 18
#     if s > 0:
#         z = (s - 1) / np.sqrt(var_s)
#     elif s < 0:
#         z = (s + 1) / np.sqrt(var_s)
#     else:
#         z = 0
#     p_value = 2 * (1 - norm.cdf(abs(z)))
#     return z, p_value
#
# # 绘制柱状图函数，包括趋势线和分界线
# def plot_data_with_trends_bars(columns_to_plot):
#     fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(30, 22.5))
#     axes = axes.flatten()
#
#     # 分界线数据及其标签
#     threshold_lines = {
#         '溶解氧': [(7.5, 'Ⅰ')],
#         '高锰酸盐指数': [(4, 'Ⅰ'), (6, 'Ⅱ')],
#         '氨氮': [(0.15, 'Ⅰ'), (0.5, 'Ⅱ')],
#         '总磷': [(0.1, 'Ⅰ'), (0.2, 'Ⅱ')],
#         '总氮': [(2.0, 'Ⅴ')]
#     }
#
#     for idx, col in enumerate(columns_to_plot):
#         y = filtered_monthly_data[col].dropna()
#         x = np.arange(len(y))
#
#         # 绘制柱状图，条件着色
#         #bar_colors = ['red' if value < threshold_lines[col][0][0] else 'skyblue' for value in y] if col in threshold_lines else 'skyblue'
#         axes[idx].bar(y.index, y, color='skyblue', width=1.0)
#
#         # 为每个指定的列添加黑色细虚线分界线，不加入图例
#         if col in threshold_lines:
#             for line, label in threshold_lines[col]:
#                 axes[idx].axhline(y=line, color='black', linestyle='--', linewidth=1)
#                 axes[idx].text(y.index[-1], line, f' {label}', va='center', ha='right', backgroundcolor='white')
#
#             # 线性趋势线
#             slope, intercept = np.polyfit(x, y, 1)
#             trend_line = slope * x + intercept
#             trend_equation = f"y = {slope:.2f}x + {intercept:.2f}"
#
#             # 趋势检测
#             z_value, p_value = mann_kendall_test(y)
#             trend_details = f"Z: {z_value:.2f}, P: {p_value:.3f}"
#
#             # 绘制趋势线
#             axes[idx].plot(y.index, trend_line, color='red', linestyle='--', label='趋势线')
#
#             # 添加趋势方程和Z、P值注释
#             axes[idx].annotate(f"{trend_equation}\n{trend_details}", xy=(0.95, 0.95), xycoords='axes fraction',
#                                fontsize=12,
#                                horizontalalignment='right', verticalalignment='top',
#                                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="b", lw=2))
#
#         axes[idx].set_ylabel(col)
#         axes[idx].legend(loc='upper left')
#
#     plt.tight_layout()
#     plt.show()
#
# # List of columns to plot (replace with actual column names)
# columns_to_plot = ['水温','pH', '溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮','电导率','浊度']
# plot_data_with_trends_bars(columns_to_plot)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# 设置中文和负号正确显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取CSV文件（使用GBK编码）
file_path = 'E:\\素材2\\资料\\统计建模数据 (3)\\all.csv'
data = pd.read_csv(file_path, encoding='GBK')

# 处理监测时间列
data['监测时间'] = pd.to_datetime(data['监测时间'], errors='coerce')

# 选择包含数值和时间列的数据
numeric_cols_with_time = data.select_dtypes(include=[np.number, 'datetime'])

# 使用监测时间列进行重采样，计算每周的平均值
filtered_weekly_data = numeric_cols_with_time.resample('W', on='监测时间').mean()
filtered_weekly_data = filtered_weekly_data[filtered_weekly_data.index >= "2021-01-01"]

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

# 绘制柱状图函数，包括趋势线和分界线
def plot_data_with_trends_bars(columns_to_plot):
    fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(20, 60))
    axes = axes.flatten()

    # 分界线数据及其标签（根据需要添加各指标的标准线）
    threshold_lines = {
        '溶解氧': [(7.5, 'Ⅰ')],
        '高锰酸盐指数': [(4, 'Ⅰ'), (6, 'Ⅱ')],
        '氨氮': [(0.15, 'Ⅰ'), (0.5, 'Ⅱ')],
        '总磷': [(0.1, 'Ⅰ'), (0.2, 'Ⅱ')],
        '总氮': [(2.0, '')],
        'WQI-DET': [(20, 'IⅤ'),(40, 'III')]
        # 水温、浊度、电导率通常没有固定标准线，如需添加请在此补充
    }

    for idx, col in enumerate(columns_to_plot):
        y = filtered_weekly_data[col].dropna()
        x = np.arange(len(y))

        # 绘制柱状图
        axes[idx].bar(y.index, y, color='skyblue', width=1.0)

        # 添加分界线（如果该指标有标准线）
        if col in threshold_lines:
            for line, label in threshold_lines[col]:
                axes[idx].axhline(y=line, color='black', linestyle='--', linewidth=1)
                axes[idx].text(y.index[-1], line, f' {label}', va='center', ha='right', backgroundcolor='white')

        # 对所有指标绘制趋势线（包括pH）
        # 线性趋势线
        slope, intercept = np.polyfit(x, y, 1)
        trend_line = slope * x + intercept
        trend_equation = f"y = {slope:.2f}x + {intercept:.2f}"

        # 趋势检测
        z_value, p_value = mann_kendall_test(y)
        trend_details = f"Z: {z_value:.2f}, P: {p_value:.3f}"

        # 绘制趋势线
        axes[idx].plot(y.index, trend_line, color='red', linestyle='--', label='趋势线')

        # 添加趋势方程和Z、P值注释
        axes[idx].annotate(f"{trend_equation}\n{trend_details}", xy=(0.95, 0.95), xycoords='axes fraction',
                          fontsize=12,
                          horizontalalignment='right', verticalalignment='top',
                          bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="b", lw=2))

        axes[idx].set_ylabel(col)
        axes[idx].legend(loc='upper left')

    # 隐藏多余的子图
    for i in range(len(columns_to_plot), len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

# 需要绘制的指标列（新增水温、浊度、电导率）
columns_to_plot = [ 'pH', '溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮','WQI-DET' ]
# 只保留数据中实际存在的列
columns_to_plot = [col for col in columns_to_plot if col in filtered_weekly_data.columns]
plot_data_with_trends_bars(columns_to_plot)