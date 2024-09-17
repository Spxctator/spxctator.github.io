import pandas as pd

# Define the file paths
file_path = '.data/annual-area-burnt-by-wildfires.csv'
filtered_file_path = '.data/annual-area-burnt-by-wildfires-2020.csv'

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Filter the data for the year 2020
df_2020 = df[df["Year"] == 2020]

# Save the filtered data to a new CSV file
df_2020.to_csv(filtered_file_path, index=False)

# Print a confirmation message
print(f"Filtered data for the year 2020 has been saved to '{filtered_file_path}'.")
