import pandas as pd  # Import the pandas library for data manipulation

# Define the file paths
file_path = '.data/average-monthly-surface-temperature.csv'  # Path to the original temperature dataset
filtered_file_path = '.data/average-monthly-surface-temperature-2020.csv'  # Path to save the filtered dataset

# Load the dataset into a DataFrame
df_temp = pd.read_csv(file_path)

# Filter the data for the year 2020
df_temp_2020 = df_temp[df_temp["year"] == 2020]

# Calculate the average surface temperature for each country in 2020 for "Average surface temperature"
average_temp_per_country_2020_year = df_temp_2020.groupby(["Entity", "Code"])["Average surface temperature"].mean().reset_index()

# Round the averages to 2 decimal places
average_temp_per_country_2020_year["Average surface temperature"] = average_temp_per_country_2020_year["Average surface temperature"].round(2)

# Save the average temperatures to a new CSV file
average_temp_per_country_2020_year.to_csv(filtered_file_path, index=False)

# Print a confirmation message
print(f"Average surface temperatures per country for the year 2020 have been saved to '{filtered_file_path}'.")
