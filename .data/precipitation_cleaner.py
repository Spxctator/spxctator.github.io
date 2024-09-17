import pandas as pd  # Import the pandas library for data manipulation

# Define the file paths
file_path = '.data/average-precipitation-per-year.csv'  # Path to the original precipitation dataset
filtered_file_path = '.data/average-precipitation-per-year-2020.csv'  # Path to save the filtered dataset

# Load the dataset into a DataFrame
df_temp = pd.read_csv(file_path)  # Read the CSV file into a pandas DataFrame

# Filter the data for the year 2020
df_temp_2020 = df_temp[df_temp["Year"] == 2020]  # Select rows where the "Year" column is 2020

# Calculate the average precipitation for each country in 2020
average_precipitation_per_country_2020 = df_temp_2020.groupby(["Entity", "Code"])["Average precipitation in depth (mm per year)"].mean().reset_index()  # Group by "Entity" and "Code" and calculate the mean

# Round the averages to 2 decimal places
average_precipitation_per_country_2020["Average precipitation in depth (mm per year)"] = average_precipitation_per_country_2020["Average precipitation in depth (mm per year)"].round(2)  # Round the precipitation values to 2 decimal places

# Save the average precipitation to a new CSV file
average_precipitation_per_country_2020.to_csv(filtered_file_path, index=False)  # Write the DataFrame to a new CSV file without the index

# Print a confirmation message
print(f"Average precipitation per country for the year 2020 has been saved to '{filtered_file_path}'.")  # Output a message confirming the save
