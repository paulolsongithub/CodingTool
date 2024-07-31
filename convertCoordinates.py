import pandas as pd

# Read the input CSV file
input_file = r'Event Data.xlsx' 
df = pd.read_excel(input_file, sheet_name=0)

# Create a new dataframe to store the result
result = pd.DataFrame(columns=['Game Id', 'Id', 'Path', 'x', 'y', 'z'])

# Process each row
for index, row in df.iterrows():
    game_id_value = row['Game Id']
    id_value = row['Id']
    start_x = row['Start Location X']
    start_y = row['Start Location Y']
    end_x = row['End Location X']
    end_y = row['End Location Y']
    end_z = row['End Location Z']
    
    # Append starting location with path = 1
    result = result.append({'Game Id': game_id_value, 'Id': id_value, 'Path': 1, 'x': start_x, 'y': start_y, 'z': None}, ignore_index=True)
    
    # Append ending location with path = 2
    result = result.append({'Game Id': game_id_value,'Id': id_value, 'Path': 2, 'x': end_x, 'y': end_y, 'z': end_z}, ignore_index=True)

# Write the result to a new CSV file
output_file = r'convertedCoordinates.csv'  # replace with your desired output file name
result.to_csv(output_file, index=False)

print(f"Processed data has been saved to {output_file}")
