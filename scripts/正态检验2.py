import pandas as pd
from scipy import stats

# 载入数据
file_path = 'local-inputs/副本数据2.xlsx'
excel_data = pd.ExcelFile(file_path)
data = excel_data.parse('数据2')

# 要进行正态性检验的列
columns_to_test = ['水温', 'pH', '溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮', '电导率', '浊度']

# D’Agostino-Pearson检验
normality_results = {}

for column in columns_to_test:
    # 去除NaN值
    data_column = data[column].dropna()

    # D’Agostino-Pearson正态性检验
    stat, p_value = stats.normaltest(data_column)

    # 存储结果
    normality_results[column] = {
        'Statistic': stat,
        'P-value': p_value,
        'Normal': p_value > 0.05  # p值 > 0.05，表示数据符合正态分布
    }

# 将结果转换为DataFrame，方便查看
normality_df = pd.DataFrame(normality_results).T
print(normality_df)
