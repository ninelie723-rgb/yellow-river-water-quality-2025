import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skill_metrics as sm

# 读取数据
data = pd.read_excel('time.xlsx')

# 提取数据
models = data['Model'].values
sd_values = data['SD'].values
rmse_values = data['RMSE'].values
r_squared_values = data['R-Squared'].values

# 计算相关系数 R
r_values = np.sqrt(r_squared_values)

# 观测数据的标准差
observed_sd = 32.9569262504085

# 创建泰勒图所需的数据
sdev = np.concatenate(([observed_sd], sd_values))  # 观测数据标准差作为第一个元素
crmsd = np.concatenate(([0], rmse_values))  # 将 RMSE 以模型的顺序进行插入，第一个元素是0
ccoef = np.concatenate(([1], r_values))  # 相关系数以1作为第一个元素代表观测数据的相关性

MARKERS = {
    "ExtraTreesRegressor": {
        "labelColor": "k",
        "symbol": ".",
        "size": 9,
        "faceColor": "r",
        "edgeColor": "r",
    },
    "RandomForestRegressor": {
        "labelColor": "gray",
        "symbol": ".",
        "size": 9,
        "faceColor": "b",
        "edgeColor": "b",
    },
    "BaggingRegressor": {
        "labelColor": "k",
        "symbol": ".",
        "size": 9,
        "faceColor": "g",
        "edgeColor": "g",
    },
    "XGBRegressor": {
        "labelColor": "gray",
        "symbol": ".",
        "size": 9,
        "faceColor": "c",
        "edgeColor": "c",
    },
    "LGBMRegressor": {
        "labelColor": "k",
        "symbol": ".",
        "size": 9,
        "faceColor": "m",
        "edgeColor": "m",
    },
    "HistGradientBoostingRegressor": {
        "labelColor": "gray",
        "symbol": ".",
        "size": 9,
        "faceColor": "y",
        "edgeColor": "y",
    },
    "DecisionTreeRegressor": {
        "labelColor": "k",
        "symbol": "*",
        "size": 9,
        "faceColor": "r",
        "edgeColor": "r",
    },
    "KNeighborsRegressor": {
        "labelColor": "gray",
        "symbol": "*",
        "size": 9,
        "faceColor": "b",
        "edgeColor": "b",
    },
    "ExtraTreeRegressor": {
        "labelColor": "k",
        "symbol": "*",
        "size": 9,
        "faceColor": "g",
        "edgeColor": "g",
    },
    "MLPRegressor": {
        "labelColor": "gray",
        "symbol": "*",
        "size": 9,
        "faceColor": "c",
        "edgeColor": "c",
    },
    "GradientBoostingRegressor": {
        "labelColor": "k",
        "symbol": "*",
        "size": 9,
        "faceColor": "m",
        "edgeColor": "m",
    },
    "NuSVR": {
        "labelColor": "gray",
        "symbol": "*",
        "size": 9,
        "faceColor": "y",
        "edgeColor": "y",
    },
    "SVR": {
        "labelColor": "k",
        "symbol": "^",
        "size": 7,
        "faceColor": "r",
        "edgeColor": "r",
    },
    "LinearSVR": {
        "labelColor": "gray",
        "symbol": "^",
        "size": 7,
        "faceColor": "b",
        "edgeColor": "b",
    },
    "AdaBoostRegressor": {
        "labelColor": "k",
        "symbol": "^",
        "size": 7,
        "faceColor": "g",
        "edgeColor": "g",
    },
    "PassiveAggressiveRegressor": {
        "labelColor": "gray",
        "symbol": "^",
        "size": 7,
        "faceColor": "c",
        "edgeColor": "c",
    },
    "OrthogonalMatchingPursuit": {
        "labelColor": "k",
        "symbol": "^",
        "size": 7,
        "faceColor": "m",
        "edgeColor": "m",
    },
    "RANSACRegressor": {
        "labelColor": "gray",
        "symbol": "^",
        "size": 7,
        "faceColor": "y",
        "edgeColor": "y",
    },
    "PoissonRegressor": {
        "labelColor": "k",
        "symbol": "s",
        "size": 7,
        "faceColor": "r",
        "edgeColor": "r",
    },
    "TweedieRegressor": {
        "labelColor": "gray",
        "symbol": "s",
        "size": 7,
        "faceColor": "b",
        "edgeColor": "b",
    },
    "GammaRegressor": {
        "labelColor": "k",
        "symbol": "s",
        "size": 7,
        "faceColor": "g",
        "edgeColor": "g",
    },
    # "17437": {
    #     "labelColor": "gray",
    #     "symbol": ".",
    #     "size": 9,
    #     "faceColor": "c",
    #     "edgeColor": "c",
    # },
}

# 设置matplotlib 基本配置
plt.figure(figsize=(16, 10))

# 创建泰勒图
sm.taylor_diagram(sdev, crmsd, ccoef, markers=MARKERS,
                  markerLegend='on',
                  colOBS='k',styleOBS = ':',
                  titleOBS='Observation',
                  markerLabelColor='r',
                  tickRMS=np.arange(10, 31, 10),
                  tickRMSangle=110.0,
                  colRMS='k', styleRMS=':', widthRMS=2.0,titleRMS = 'off',
                  tickSTD=np.arange(0, 41, 10), axismax=40,titleSTD = 'off',
                  colSTD='k', styleSTD='-.', widthSTD=1.0,
                  colCOR='k', styleCOR='--', widthCOR=1.0,)
# sm.taylor_diagram(sdev, crmsd, ccoef, markers=MARKERS,  markerLegend='on',
#                    styleOBS='-', colOBS='r', markerobs='o',
#                   tickRMS=[0.0, 1.0, 2.0, 3.0],
#                   tickRMSangle=115, showlabelsRMS='on',
#                   titleRMS='on', titleOBS='Ref')

# 显示图像
plt.show()
