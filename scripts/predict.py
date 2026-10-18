import pandas as pd
from lazypredict.Supervised import LazyRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# 加载数据（确保路径正确）
data = pd.read_csv('average_data_with_grade.csv', encoding='GBK')


# 确保“监测时间”列是日期时间格式
data["监测时间"] = pd.to_datetime(data["监测时间"], errors='coerce')

# 删除包含NaT的行
data = data.dropna(subset=["监测时间"])

# 将“监测时间”列转化为日期格式，并提取年份、月份、日期等特征
data["年份"] = data["监测时间"].dt.year
data["月份"] = data["监测时间"].dt.month
data["日期"] = data["监测时间"].dt.day
#data['hour'] = data['监测时间'].dt.hour
# label_encoder = LabelEncoder()
# data['断面名称_encoded'] = label_encoder.fit_transform(data['断面名称'])
# 查看处理后的数据
print(data.head())

# 提取相关特征和目标变量
X = data[['年份', '月份', '日期','断面名称']]
y = data['wqi']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用LazyRegressor进行模型拟合
lazy_regressor = LazyRegressor()
models = lazy_regressor.fit(X_train, X_test, y_train, y_test)

# 计算真实值的标准差（假设目标变量为 'wqi'）
sigma_r = y_train.std()

print(f"真实值的标准差 σr: {sigma_r}")
# 打印模型的拟合结果
print(models)

