import pandas as pd

# Function to read data from the input CSV file and calculate yearly totals
def calculate_yearly_totals(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Filter the data for the years 2012 to 2022
    df_filtered = df[(df['Year'] >= 2012) & (df['Year'] <= 2022)]
    
    # Group by 'Year' and sum the 'Annual area burnt by wildfires'
    yearly_totals = df_filtered.groupby('Year')['Annual area burnt by wildfires'].sum().reset_index()
    
    # Save the results to a new CSV file
    yearly_totals.to_csv(output_file, index=False)
    
    print(f"The total area burnt by wildfires for each year from 2012 to 2022 has been saved to '{output_file}'.")

# Specify the input and output file names
input_file = '.data/annual-area-burnt-by-wildfires.csv'
output_file = '.data/annual-area-burnt-by-wildfires-2012-2022.csv'

# Call the function to perform the calculation and save the results
calculate_yearly_totals(input_file, output_file)
