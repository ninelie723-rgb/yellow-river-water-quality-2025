import pandas as pd

# Load the dataset with the correct encoding (e.g., gbk)
file_path = 'local-inputs/ALL_cleaned_gbk.csv'
data = pd.read_csv(file_path, encoding='gbk')

# Select the relevant columns for Spearman correlation analysis
columns_of_interest = ['pH', '溶解氧', '高锰酸盐指数', '氨氮', '总磷', '总氮']

# Calculate the Spearman correlation matrix
spearman_corr = data[columns_of_interest].corr(method='spearman')

# Display the Spearman correlation matrix
print(spearman_corr)
