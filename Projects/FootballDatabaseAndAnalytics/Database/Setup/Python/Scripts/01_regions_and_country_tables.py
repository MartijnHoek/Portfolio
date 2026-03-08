from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from CountryDefinitions.Countries import Countries
from CountryDefinitions.Regions import Regions

sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM regions;")
sql_handler.cursor.execute("DELETE FROM countries;")

# Fill the region table with regions defined in Regions.py
for name, region in vars(Regions).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO regions (uuid, name) VALUES (%s, %s);", (region.uuid, region.name))

sql_handler.get_result("regions")

# Save changes
sql_handler.save_table_changes()

for name, country in vars(Countries).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO countries VALUES (%s, %s, %s);", (country.uuid, country.name, country.region.uuid))

sql_handler.get_result("countries")

# Save changes
sql_handler.save_table_changes()