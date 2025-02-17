import pandas as pd

loadTuebinden = True

# Load the dataset from a CSV file
if (loadTuebinden):
    raw_data = pd.read_csv("../data/raw_game_data_tigers.csv")
else:
    raw_data = pd.read_csv("../data/raw_game_data_heidelberg.csv")

date_object = pd.to_datetime(raw_data["date"], format="%d.%m.%Y")

# Add the weekday of the game with the help of the date
raw_data["weekday"] = date_object.dt.day_name()

# Calculate rest days between matches
raw_data["rest_days"] = date_object.diff().dt.days.fillna(0).astype(int)


# convert specific columns from string to float
columns = [
    "arena_occupancy",
    "2_pointer_percentage",
    "3_pointer_percentage",
    "free_throw_percentage",
]

if (loadTuebinden):
    columns.append("jackson_minutes_played")
else:
    columns.append("jaworski_minutes_played")

for column in columns:
    raw_data[column] = raw_data[column].str.replace(",", ".").astype(float)

# Save the processed data to a new file
if (loadTuebinden):
    raw_data.to_csv("../data/processed_data_tigers.csv", index=False,)
else:
    raw_data.to_csv("../data/processed_data_heidelberg.csv", index=False,)
