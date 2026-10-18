import pandas as pd
import numpy as np
from scipy.stats import bartlett
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load the dataset
file_path = 'local-inputs/绿色.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Function to calculate KMO statistic


# Function to perform Bartlett's test of sphericity
def bartlett_test(data):
    # Perform Bartlett's test on the correlation matrix
    chi_square_value, p_value = bartlett(*[data[col] for col in data.columns])
    return chi_square_value, p_value

# Extracting the relevant columns for analysis
variables_to_analyze_3 = [
    '高锰酸盐指数', '总氮', '总磷', '氟化物', '六价铬', '氰化物'
]
data_selected_3 = df[variables_to_analyze_3]

# Dropping rows with missing values
data_selected_clean_3 = data_selected_3.dropna()

# Calculate the correlation matrix for the selected variables
correlation_matrix_selected_3 = data_selected_clean_3.corr()


# Bartlett's test of sphericity
bartlett_chi_square_selected_3, bartlett_p_value_selected_3 = bartlett_test(data_selected_clean_3)

# Output the results
print(f"Bartlett's Chi-square: {bartlett_chi_square_selected_3}")
print(f"Bartlett's p-value: {bartlett_p_value_selected_3}")

# Display the correlation matrix
print("Correlation Matrix:\n", correlation_matrix_selected_3)
