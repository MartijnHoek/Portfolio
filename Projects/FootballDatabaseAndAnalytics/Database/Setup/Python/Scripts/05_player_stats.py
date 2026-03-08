from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from CareerModeData.PlayerList import PlayerList

sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM physical_stats;")
sql_handler.cursor.execute("DELETE FROM mental_stats;")
sql_handler.cursor.execute("DELETE FROM technical_stats;")
sql_handler.cursor.execute("DELETE FROM goalkeeping_stats;")

# Physical stats
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    acceleration = player.physical_stats.acceleration
    agility = player.physical_stats.agility
    balance = player.physical_stats.balance
    jumping = player.physical_stats.jumping
    reactions = player.physical_stats.reactions
    sprint_speed = player.physical_stats.sprint_speed
    stamina = player.physical_stats.stamina
    strength = player.physical_stats.strength

    sql_handler.cursor.execute("INSERT INTO physical_stats "
                               "(uuid, acceleration, agility, balance, jumping,"
                               " reactions, sprint_speed, stamina, strength) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                               (uuid, acceleration, agility, balance, jumping,
                                 reactions, sprint_speed, stamina, strength))

sql_handler.get_result("physical_stats")

# Save changes
sql_handler.save_table_changes()

# Mental stats
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    aggression = player.mental_stats.aggression
    att_positioning = player.mental_stats.att_positioning
    composure = player.mental_stats.composure
    interceptions = player.mental_stats.interceptions
    vision = player.mental_stats.vision

    sql_handler.cursor.execute("INSERT INTO mental_stats "
                               "(uuid, aggression, att_positioning, composure, interceptions, vision) "
                               "VALUES (%s, %s, %s, %s, %s, %s);",
                               (uuid, aggression, att_positioning, composure, interceptions, vision))

sql_handler.get_result("mental_stats")

# Save changes
sql_handler.save_table_changes()

# Technical stats
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    ball_control = player.technical_stats.ball_control
    crossing = player.technical_stats.crossing
    curve = player.technical_stats.curve
    def_awareness = player.technical_stats.def_awareness
    dribbling = player.technical_stats.dribbling
    fk_accuracy = player.technical_stats.fk_accuracy
    finishing = player.technical_stats.finishing
    heading_accuracy = player.technical_stats.heading_accuracy
    long_pass = player.technical_stats.long_pass
    long_shots = player.technical_stats.long_shots
    penalties = player.technical_stats.penalties
    short_pass = player.technical_stats.short_pass
    shot_power = player.technical_stats.shot_power
    slide_tackle = player.technical_stats.slide_tackle
    stand_tackle = player.technical_stats.stand_tackle
    volleys = player.technical_stats.volleys

    sql_handler.cursor.execute("INSERT INTO technical_stats "
                               "(uuid, ball_control, crossing, curve, def_awareness, dribbling, fk_accuracy, finishing,"
                               "heading_accuracy, long_pass, long_shots, penalties, short_pass, shot_power, slide_tackle,"
                               "stand_tackle, volleys) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                               (uuid, ball_control, crossing, curve, def_awareness, dribbling, fk_accuracy, finishing,
                                heading_accuracy, long_pass, long_shots, penalties, short_pass, shot_power, slide_tackle,
                                stand_tackle, volleys))

sql_handler.get_result("technical_stats")

# Save changes
sql_handler.save_table_changes()

# Goalkeeping stats
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    gk_diving = player.goalkeeping_stats.gk_diving
    gk_handling = player.goalkeeping_stats.gk_handling
    gk_kicking = player.goalkeeping_stats.gk_kicking
    gk_positioning = player.goalkeeping_stats.gk_positioning
    gk_reflexes = player.goalkeeping_stats.gk_reflexes

    sql_handler.cursor.execute("INSERT INTO goalkeeping_stats"
                               "(uuid, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes) "
                               "VALUES (%s, %s, %s, %s, %s, %s);",
                               (uuid, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes))

sql_handler.get_result("goalkeeping_stats")

# Save changes
sql_handler.save_table_changes()