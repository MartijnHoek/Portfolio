from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from PlayerDefinitions.CareerInfo import FifaVersion, Clubs, CareerMode

sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM career_modes;")
sql_handler.cursor.execute("DELETE FROM clubs;")
sql_handler.cursor.execute("DELETE FROM game_versions;")

for name, fifa_version in vars(FifaVersion).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO game_versions (uuid, name) VALUES (%s, %s);", (fifa_version.uuid, fifa_version.name))

sql_handler.get_result("game_versions")

# Save changes
sql_handler.save_table_changes()

for name, club in vars(Clubs).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO clubs (uuid, name, country_uuid) VALUES (%s, %s, %s);", (club.uuid, club.name, club.country.uuid))

sql_handler.get_result("clubs")

# Save changes
sql_handler.save_table_changes()


for name, career_mode in vars(CareerMode).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO career_modes (uuid, game_version_uuid, year, club_uuid) VALUES (%s, %s, %s, %s);",
                                   (career_mode.uuid, career_mode.fifa_version.uuid, career_mode.career_mode_year, career_mode.club.uuid))

sql_handler.get_result("career_modes")

# Save changes
sql_handler.save_table_changes()
