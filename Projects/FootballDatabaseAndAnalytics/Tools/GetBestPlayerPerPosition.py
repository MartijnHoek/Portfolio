from CareerModeData.PlayerList import PlayerList


best_players = {
    "gk":   None,
    "cb":   None,
    "rb":   None,
    "lb":   None,
    "lwb":  None,
    "rwb":  None,
    "cdm":  None,
    "cm":   None,
    "lm":   None,
    "rm":   None,
    "cam":  None,
    "cf":   None,
    "lw":   None,
    "rw":   None,
    "st":   None,
}

# loop through all players
for player in PlayerList.PLAYERS:
    for position, current_best in best_players.items():
        player_rating = getattr(player.ratings, position)

        if current_best is None:
            # no best yet → this player becomes best by default
            best_players[position] = (player, player_rating)
        else:
            best_player, best_rating = current_best
            if player_rating > best_rating:
                best_players[position] = (player, player_rating)


# Best player per position
print("Best player per position with duplicates")
for pos, (player, rating) in best_players.items():
    print(f"{pos.upper()}: {player.person_info.first_name} {player.person_info.last_name} ({rating}) | {player.person_info.career_mode.fifa_version} {player.person_info.career_mode.club}")


# Example: 4-3-3 formation
formation = {
    "gk":   1,
    "cb":   2,
    "rb":   1,
    "lb":   1,
    "cm":   2,
    "cam":  1,
    "rw":   1,
    "st":   1,
    "lw":   1,
}

best_team = {pos: [] for pos in formation.keys()}
assigned_uuids = set()

for position, slots in formation.items():
    for _ in range(slots):  # loop for each slot
        best_player = None
        best_rating = -1

        for player in PlayerList.PLAYERS:
            player_uuid = player.person_info.uuid
            if player_uuid in assigned_uuids:
                continue  # skip already used players

            rating = getattr(player.ratings, position, None)
            if rating is not None and rating > best_rating:
                best_rating = rating
                best_player = player

        if best_player:
            best_team[position].append((best_player, best_rating))
            assigned_uuids.add(best_player.person_info.uuid)

print("")
print("")
print("Best formation-based team (no duplicates):")
for pos, players in best_team.items():
    for player, rating in players:
        print(f"{pos.upper()}: {player.person_info.first_name} {player.person_info.last_name} ({rating}) | {player.person_info.career_mode.fifa_version} {player.person_info.career_mode.club}")
