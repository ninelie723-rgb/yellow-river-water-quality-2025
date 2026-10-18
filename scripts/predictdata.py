import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split

# 加载数据（确保路径正确）
data = pd.read_csv('average_data_with_grade.csv', encoding='GBK')

# 重命名列名
data.columns = ['地点', '监测时间', '溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮', 'WQI','水质等级']

# 提取相关特征和目标变量
X = data[['溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮']]
y = data['水质等级']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用LazyRegressor进行模型拟合
lazy_regressor = LazyRegressor()
models = lazy_regressor.fit(X_train, X_test, y_train, y_test)

# 计算真实值的标准差（假设目标变量为 '水质等级'）
sigma_r = data['水质等级'].std()

print(f"真实值的标准差 σr: {sigma_r}")
# 打印模型的拟合结果
print(models)
