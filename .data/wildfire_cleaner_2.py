import pandas as pd
from countryinfo import CountryInfo

# Define the file paths
file_path = '.data/annual-area-burnt-by-wildfires-2020.csv'
filtered_file_path = '.data/annual-area-burnt-by-wildfires-2020-n.csv'

# Load the dataset into a DataFrame
df = pd.read_csv(file_path)

# Function to get the area of a country using CountryInfo library
def get_country_area(country_name):
    try:
        country = CountryInfo(country_name)
        return country.info().get('area', float('nan'))
    except KeyError:
        return float('nan')

# Apply the function to get the area of each country and normalize the area burnt
df['Country Area'] = df['Entity'].apply(get_country_area)
df['Normalized area burnt'] = (df['Annual area burnt by wildfires'] / df['Country Area'])

# Save the filtered data to a new CSV file
df.to_csv(filtered_file_path, index=False)

# Print a confirmation message
print(f"Filtered data for the year 2020 has been saved to '{filtered_file_path}'.")
