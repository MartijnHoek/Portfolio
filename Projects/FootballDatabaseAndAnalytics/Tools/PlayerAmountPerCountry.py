from CareerModeData.PlayerList import PlayerList


seen_nations = {}
for player in PlayerList.PLAYERS:
    nationality = player.person_info.nationality

    if nationality.name not in seen_nations.keys():
        seen_nations[nationality.name] = 1
    elif nationality.name in seen_nations.keys():
        seen_nations[nationality.name] = seen_nations[nationality.name] + 1

complete_squad_nations = []
complete_lineup_nations = []
for nation, count in seen_nations.items():
    if count >= 23:     # Complete team with starting 11 and substitutes and enough reserves for squad depth
        complete_squad_nations.append(nation)
    elif count >= 11:   # Only enough players to have a starting 11 but not enough squad depth
        complete_lineup_nations.append(nation)

print(f"Total player count is: {len(PlayerList.PLAYERS)}")

print("")

print("The total player per nation count is: ")
# Sort nations alphabetically
for nation in sorted(seen_nations.keys()):
    print(f"{nation}: {seen_nations[nation]}")

print("")

# Only enough players to have a starting 11 but not enough squad depth
if len(complete_lineup_nations) != 0:
    print("Nations with enough players to create a lineup are:")
    for eligible_nation in complete_lineup_nations:
        print(f"{eligible_nation}: {seen_nations[eligible_nation]}")

print("")

# Complete team with starting 11 and substitutes and enough reserves for squad depth
if len(complete_squad_nations) != 0:
    print("Nations with enough players to create a squad are:")
    for eligible_nation in complete_squad_nations:
        print(f"{eligible_nation}: {seen_nations[eligible_nation]}")


