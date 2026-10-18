import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
file_path = r'E:\素材2\资料\统计建模数据 (3)\千河公路桥.csv'  # 替换为正确的文件路径
data = pd.read_csv(file_path,encoding='gbk')

# 转换监测时间为可用的特征
data['监测时间'] = pd.to_datetime(data['监测时间'], errors='coerce')
data.dropna(subset=['WQI-DET', '监测时间'], inplace=True)
data['年'] = data['监测时间'].dt.year
data['月'] = data['监测时间'].dt.month
data['日'] = data['监测时间'].dt.day
data['小时'] = data['监测时间'].dt.hour

# 选择特征和目标变量
features = data[['年', '月', '日', '小时']]
target = data["WQI-DET"]

# 删除缺失值
features = features[target.notna()]
target = target[target.notna()]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 初始化极端随机森林回归器
model = ExtraTreesRegressor(n_estimators=100, random_state=42)

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 创建未来90天的日期特征数据集
future_dates = pd.date_range(start='2025-05-01', periods=90, freq='D')
future_features = pd.DataFrame({
    '年': future_dates.year,
    '月': future_dates.month,
    '日': future_dates.day,
    '小时': [0]*len(future_dates)  # 假设小时为0
})

# 确保未来数据的特征顺序与训练数据一致
future_features = future_features[features.columns]

# 使用训练好的模型对未来数据进行预测
future_predictions = model.predict(future_features)

# 输出预测结果
future_results = future_features.copy()
future_results['预测WQI-DET'] = future_predictions

# 保存结果为Excel文件
future_results.to_excel(r'E:\素材2\资料\统计建模数据 (3)\千河公路桥WQI预测.xlsx', index=False)

print("预测结果已保存为Excel文件。")
