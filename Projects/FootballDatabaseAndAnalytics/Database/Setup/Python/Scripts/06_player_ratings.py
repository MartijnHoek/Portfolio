from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler
from CareerModeData.PlayerList import PlayerList

sql_handler = SqlHandler()

# Table should be empty but delete everything to be sure
sql_handler.cursor.execute("DELETE FROM player_ratings;")

# Player positional ratings
for player in PlayerList.PLAYERS:
    uuid = player.person_info.uuid
    gk = player.ratings.gk
    cb = player.ratings.cb
    lb_rb = player.ratings.lb   # rb is the same
    lwb_rwb = player.ratings.lwb
    cdm = player.ratings.cdm
    cm = player.ratings.cm
    lm_rm = player.ratings.lm   # rm is the same
    cam = player.ratings.cam
    cf = player.ratings.cf
    lw_rw = player.ratings.lw   # rw is the same
    st = player.ratings.st

    sql_handler.cursor.execute("INSERT INTO player_ratings "
                               "(uuid, gk, cb, lb_rb, lwb_rwb,"
                               " cdm, cm, lm_rm, cam, cf, lw_rw, st) "
                               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                               (uuid, gk, cb, lb_rb, lwb_rwb,
                                cdm, cm, lm_rm, cam, cf, lw_rw, st))

sql_handler.get_result("player_ratings")

# Save changes
sql_handler.save_table_changes()
