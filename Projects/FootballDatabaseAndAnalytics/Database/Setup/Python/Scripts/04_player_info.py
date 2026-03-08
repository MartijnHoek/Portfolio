from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from CareerModeData.PlayerList import PlayerList
from PlayerDefinitions.PlayerObject import Traits

def height_conversion(height_dict: dict[str, int]) -> int:
    """
    Converts the height in inches into centimeters
    :param height_dict: Height dictionary in inches and feet
    :return: Height in centimeters
    """
    inches = height_dict["inches"]
    feet = height_dict["feet"]
    return round((feet * 12 + inches) * 2.54)

def weight_conversion(weight_lbs: int) -> int:
    """
    Converts the weight in lbs into kg
    :param weight_lbs: Weight in lbs
    :return: Weight in kg
    """
    return round(weight_lbs * 0.453592)


sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM player_traits;")
sql_handler.cursor.execute("DELETE FROM player_info;")
sql_handler.cursor.execute("DELETE FROM person_info;")

# Person Info
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    first_name = player.person_info.first_name
    last_name = player.person_info.last_name
    country_uuid = player.person_info.nationality.uuid
    career_mode_uuid = player.person_info.career_mode.uuid
    height_cm = height_conversion(player.person_info.height)
    weight_kg = weight_conversion(player.person_info.weight)
    birthyear = player.person_info.birthyear

    sql_handler.cursor.execute("INSERT INTO person_info "
                               "(uuid, first_name, last_name, country_uuid, career_mode_uuid,"
                               " height_cm, weight_kg, birthyear) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                               (uuid, first_name, last_name, country_uuid, career_mode_uuid,
                               height_cm, weight_kg, birthyear))

sql_handler.get_result("person_info")

# Save changes
sql_handler.save_table_changes()

# Player Traits
for player in PlayerList.PLAYERS:
    player_uuid = player.person_info.uuid
    for trait in player.player_info.traits:
        sql_handler.cursor.execute(
            "INSERT INTO player_traits (person_uuid, trait_uuid) VALUES (%s, %s)",
            (player_uuid, trait.uuid)
        )

sql_handler.get_result("player_traits")

# Save changes
sql_handler.save_table_changes()

# Player Info
for player in PlayerList.PLAYERS:
    player_uuid = player.person_info.uuid
    weak_foot = player.player_info.weak_foot
    skill_moves = player.player_info.skill_moves
    att_work_rate = player.player_info.att_work_rate
    def_work_rate = player.player_info.def_work_rate
    kit_number = player.player_info.kit_number

    sql_handler.cursor.execute(
        "INSERT INTO player_info (uuid, weak_foot, skill_moves, att_work_rate, def_work_rate, kit_number)"
        " VALUES (%s, %s, %s, %s, %s, %s)",
        (player_uuid, weak_foot, skill_moves, att_work_rate, def_work_rate, kit_number)
    )
sql_handler.get_result("player_info")

# Save changes
sql_handler.save_table_changes()