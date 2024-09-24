import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('.data/global-temperature-anomalies-by-month.csv')

# Filter the data for the years 1990 to 2020
filtered_data = data[(data['Year'] >= 1990) & (data['Year'] <= 2020)]

# Group the data by year and calculate the average temperature anomaly for each year
average_anomalies = filtered_data.groupby('Year')['Temperature anomaly'].mean()

# Convert the result to a DataFrame
average_anomalies_df = average_anomalies.reset_index()

# Save the result to a new CSV file
average_anomalies_df.to_csv('.data/global-temperature-anomalies-1990-2020.csv', index=False)

print("The average temperature anomalies have been saved to 'average-temperature-anomalies-1990-2020.csv'")
