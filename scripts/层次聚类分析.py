import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import MinMaxScaler

#设置中文和负号正确显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的意思
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
data = pd.read_csv(r'E:\素材2\资料\ALL_cleaned_gbk.csv', encoding='GBK')

# # 删除浊度和电导率列，这里假设列名分别是'Turbidity'和'Conductivity'
# data = data.drop(['浊度', '电导率'], axis=1)

# 填充缺失值
data_filled = data.fillna(data.mean())

# 计算每个断面名称的平均值
grouped_data = data_filled.groupby('断面名称').mean().reset_index()

# 层次聚类分析
linked = linkage(grouped_data.drop('断面名称', axis=1), method='ward', metric='euclidean')

# 绘制树状图
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=grouped_data['断面名称'].values, distance_sort='descending', show_leaf_counts=True)
plt.title('层次聚类树状图')
plt.xlabel('断面名称')
plt.ylabel('距离')
plt.xticks(rotation=90)
plt.show()

# 生成热图所需的排序索引
order = dendrogram(linked, no_plot=True)['ivl']
order_labels = [grouped_data.loc[int(idx), '断面名称'] for idx in order]

# 重新排序数据
sorted_data = grouped_data.set_index('断面名称').loc[order_labels]

# 数据归一化
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(sorted_data)

# 创建归一化后的数据框
normalized_df = pd.DataFrame(normalized_data, index=sorted_data.index, columns=sorted_data.columns)

# 绘制归一化后的热图
plt.figure(figsize=(8, 8))
sns.heatmap(normalized_df, cmap='YlGnBu', annot=True, fmt=".2f", linewidths=.5)
plt.title('归一化后的地点水质参数热图')
plt.ylabel('断面名称')
plt.show()

# 创建 clustermap，树状图在侧边，归一化数据
clustergrid = sns.clustermap(
    normalized_data,
    method='ward',
    cmap="coolwarm",
    figsize=(15,15 ),  # 增加图形大小以适应正方形单元格
    row_cluster=True,  # 对行（月份）进行聚类
    col_cluster=False, # 列（参数）保持原始顺序
    # cbar_pos=(1.0, 0.3, 0.02, 0.4),  # 调整图例的位置
    #square=True # 尝试使单元格为正方形
)

# 将 y 轴标签旋转为水平方向
plt.setp(clustergrid.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.setp(clustergrid.ax_heatmap.xaxis.get_majorticklabels(), rotation=0)

# 展示图形
plt.show()
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文和负号正确显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的意思
plt.rcParams['axes.unicode_minus'] = False

# 从监测时间中提取月份
data['月份'] = pd.to_datetime(data['监测时间']).dt.month

# 填充缺失值
data_filled = data.fillna(data.mean())

# 计算每个月份的平均值
grouped_data = data_filled.groupby('月份').mean().reset_index()

# 层次聚类分析
linked = linkage(grouped_data.drop('月份', axis=1), method='ward', metric='euclidean')

# 绘制树状图
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=grouped_data['月份'].values, distance_sort='descending', show_leaf_counts=True)
plt.title('层次聚类树状图（按月份）')
plt.xlabel('月份')
plt.ylabel('距离')
plt.xticks(rotation=90)
plt.show()

# 生成热图所需的排序索引
order = dendrogram(linked, no_plot=True)['ivl']
order_labels = [grouped_data.loc[int(idx), '月份'] for idx in order]

# 重新排序数据
sorted_data = grouped_data.set_index('月份').loc[order_labels]

# 数据归一化
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(sorted_data)

# 创建归一化后的数据框
normalized_df = pd.DataFrame(normalized_data, index=sorted_data.index, columns=sorted_data.columns)

# 绘制归一化后的热图
plt.figure(figsize=(8, 8))
sns.heatmap(normalized_df, cmap='YlGnBu', annot=True, fmt=".2f", linewidths=.5)
plt.title('归一化后的月份水质参数热图')
plt.ylabel('月份')
plt.show()

# 创建 clustermap，树状图在侧边，归一化数据
clustergrid = sns.clustermap(
    normalized_data,
    method='ward',
    cmap="coolwarm",
    figsize=(15,15),  # 增加图形大小以适应正方形单元格
    row_cluster=True,  # 对行（月份）进行聚类
    col_cluster=False, # 列（参数）保持原始顺序
)

# 将 y 轴标签旋转为水平方向
plt.setp(clustergrid.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.setp(clustergrid.ax_heatmap.xaxis.get_majorticklabels(), rotation=0)

# 展示图形
plt.show()
