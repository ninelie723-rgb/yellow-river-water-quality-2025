import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
import shap
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.family'] = ['SimHei']

# 读取数据
data = pd.read_csv('E:\素材2\资料\柏树林.csv', encoding='GBK')

# 假设目标变量为 '水质等级'，特征为其他列
X = data[['溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮']]  # 特征
y = data['水质等级']  # 目标变量

# 分割数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练 ExtraTreesRegressor 模型
model = ExtraTreesRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 使用 SHAP 进行特征重要性分析
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)

# 可视化特征的重要性
shap.summary_plot(shap_values, X_train)

# 可视化单个样本的 SHAP 值
# 如果需要查看单个样本的贡献，可以使用下面的代码：
# shap.initjs()
# shap.force_plot(explainer.expected_value[0], shap_values[0][0], X_train.iloc[0])
