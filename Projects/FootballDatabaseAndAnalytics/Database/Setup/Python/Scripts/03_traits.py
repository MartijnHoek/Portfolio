from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from PlayerDefinitions.PlayerObject import Traits

sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM traits;")

for name, traits in vars(Traits).items():
    # skip private and built-in attributes
    if not name.startswith("__"):
        sql_handler.cursor.execute("INSERT INTO traits (uuid, name) VALUES (%s, %s);", (traits.uuid, traits.name))

sql_handler.get_result("traits")

# Save changes
sql_handler.save_table_changes()
