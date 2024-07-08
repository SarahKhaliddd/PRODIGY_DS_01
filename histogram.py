
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('pakistan population.csv')


# Choosing column for histogram
column_name = 'Histogram of Pakistan Population (1970-2023)'  

# Step 3: Plotting histogram
plt.figure(figsize=(10, 6))  
plt.hist(df[column_name], bins=20, edgecolor='black')  
plt.xlabel('Population (in billions)')
plt.ylabel('frequency')
plt.title(f' {column_name}')
plt.grid(True)
plt.show()
