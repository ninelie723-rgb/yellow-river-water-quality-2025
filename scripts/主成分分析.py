import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.stats import bartlett

# 读取数据
file_path = ''
data = pd.read_excel(file_path, sheet_name='Sheet1')

# 选择相关列
relevant_columns = ['高锰酸盐指数', '总氮', '总磷', '氟化物', '六价铬', '氰化物']
data_relevant = data[relevant_columns]

# 提取相关列的数据并进行标准化
data_values = data_relevant.values
scaler = StandardScaler()
data_standardized = scaler.fit_transform(data_values)

# 进行巴特利球形检验
stat, p_value = bartlett(*[data_values[:, i] for i in range(data_values.shape[1])])

# 输出巴特利球形检验的结果
print("Bartlett's test statistic:", stat)
print("P-value:", p_value)

# 如果P值小于0.05，可以进行主成分分析
if p_value < 0.05:
    pca = PCA()
    pca.fit(data_standardized)

    # 获取各主成分的方差比
    explained_variance_ratio = pca.explained_variance_ratio_

    # 绘制解释的方差比例图
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio)
    plt.xlabel('主成分')
    plt.ylabel('解释的方差比例')
    plt.title('主成分方差比例图')
    plt.show()

    # 输出各主成分的方差比例
    print("Explained variance ratio:", explained_variance_ratio)

    # 获取主成分分析中的特征值
    eigenvalues = pca.explained_variance_

    # 输出特征值
    print("Eigenvalues:", eigenvalues)
else:
    print("巴特利检验未通过，数据不适合进行主成分分析。")
