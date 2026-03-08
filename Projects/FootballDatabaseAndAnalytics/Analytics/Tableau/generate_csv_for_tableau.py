
"""
Script used for getting the data from SQL merging the tables to simplify the input to Tableau.
"""
from Analytics.AnalyticsTooling import AnalyticsTooling

# Get all the dataframes
dataframe_dict = AnalyticsTooling().dataframes

# Define the dataframes
df_person_info = dataframe_dict["df_person_info"]       # done
df_player_info = dataframe_dict["df_player_info"]       # done
df_ratings = dataframe_dict["df_player_ratings"]        # done
df_career_modes = dataframe_dict["df_career_modes"]     # done
df_game_versions = dataframe_dict["df_game_versions"]   # Done
df_clubs = dataframe_dict["df_clubs"]                   # done
df_countries = dataframe_dict["df_countries"]           # Done
df_regions = dataframe_dict["df_regions"]               # Done

df_tableau_people = df_person_info.rename(columns={"uuid": "player_uuid", "country_uuid": "player_country_uuid"}).merge(
    df_player_info.rename(columns={"uuid": "player_uuid"}))

df_tableau_ratings = df_ratings.rename(columns={"uuid": "player_uuid"})

df_tableau_countries = df_countries.rename(columns={"uuid": "country_uuid", "name": "country_name"}).merge(
    df_regions.rename(columns={"uuid": "region_uuid", "name": "region_name"}))

df_tableau_career_modes = df_career_modes.rename(columns={"uuid": "career_mode_uuid"}).merge(
    df_game_versions.rename(columns={"uuid": "game_version_uuid", "name": "game_version_name"})).merge(
    df_clubs.rename(columns={"uuid": "club_uuid", "name": "club_name"}))

dataframes = {
    "people": df_tableau_people,
    "ratings": df_tableau_ratings,
    "countries": df_tableau_countries,
    "career_modes": df_tableau_career_modes
}

for name, dataframe in dataframes.items():
    dataframe.to_csv(f"exports/{name}.csv", index=False)