import pandas as pd

# Load the datasets
annual_area_burnt = pd.read_csv('.data/annual-area-burnt-by-wildfires-2020-n.csv')
average_temp = pd.read_csv('.data/average-monthly-surface-temperature-2020.csv')
average_precipitation = pd.read_csv('.data/average-precipitation-per-year-2020.csv')

# Merge the datasets on 'Entity' and 'Code'
merged_data = annual_area_burnt.merge(average_temp, on=['Entity', 'Code'], how='outer')
merged_data = merged_data.merge(average_precipitation, on=['Entity', 'Code'], how='outer')

# Save the merged dataset to a new CSV file
merged_data.to_csv('.data/merged-data-2020.csv', index=False)

print("The datasets have been successfully merged and saved to 'merged_data-2020.csv'.")
