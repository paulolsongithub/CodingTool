import pandas as pd
import sys
import os

# Define the DataFrame for storing event data
event_columns = ['Game Id', 'Event Id', 'Id', 'Period', 'Time', 'Player Number', 'Action Type', 'Type', 'Result', 'Start Location X', 'Start Location Y', 'End Location X', 'End Location Y', 'End Location Z', 'Runners']
events_df = pd.DataFrame(columns=event_columns)

class AppConfig:
    game_id = None
    player_numbers = None
    event_id = 0
    id = 0
    period = 1

def add_event_data(game_id, event_id, id, period, time, player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners):
    global events_df
    event_data = {
        'Game Id': game_id,
        'Event Id': event_id,
        'Id': id,
        'Period': period,
        'Time': time,
        'Player Number': player_number,
        'Action Type': action_type,
        'Type': type_type,
        'Result': result,
        'Start Location X': round(start_location_x, 2),
        'Start Location Y': round(start_location_y, 2),
        'End Location X': round(end_location_x, 2) if end_location_x is not None else None,
        'End Location Y': round(end_location_y, 2) if end_location_y is not None else None,
        'End Location Z': round(end_location_z, 2) if end_location_z is not None else None,
        'Runners': runners,

    }
    #events_df = pd.concat([events_df, pd.DataFrame([event_data])], ignore_index=True)
    events_df = (events_df.copy() if pd.DataFrame([event_data]).empty else pd.DataFrame([event_data]).copy() if events_df.empty
           else pd.concat([events_df, pd.DataFrame([event_data])]) # if both DataFrames non empty
           )

def save_and_exit():
    global events_df
    filename = 'event_data.csv'
    counter = 1

    # Check if the file already exists and find a new filename if it does
    while os.path.exists(filename):
        filename = f'event_data_{counter}.csv'
        counter += 1

    # Save the DataFrame to the new CSV file
    events_df.to_csv(filename, index=False)
    print(f"Event data saved to {filename}.")

    # Conditionally exit only if not in an interactive environment
    if not hasattr(sys, 'ps1'):
        sys.exit(0)
