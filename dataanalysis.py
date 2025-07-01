import pandas as pd

import matplotlib.pyplot as plt

# 1. Load CSV using Pandas
# Replace 'sales_data.csv' with your actual CSV file path
df = pd.read_csv('sales_data.csv')

# 2. Example: Group by 'Product' and sum 'Sales'
grouped = df.groupby('Product')['Sales'].sum()

# 3. Plot the results
grouped.plot(kind='bar', title='Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()