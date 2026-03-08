from SquadDefinitions import FormationHandler
from SquadDefinitions.SquadBuilder import SquadBuilder
from SquadDefinitions.SquadSelector import group_players_per_nationality, SquadInfo, NationalSquadInfo

# Get all the players in PlayerList and group them together in a dict
grouped_players_per_nation = group_players_per_nationality()
for player_list in grouped_players_per_nation.values():
    nat_squad = NationalSquadInfo(player_list)
    nat_squad.set_squad_info()

    if nat_squad.validate_squad_depth():
        print(f"This nation has enough players to build a squad: {nat_squad.squad_info.name}")
        selected_players = nat_squad.user_select_players()

        chosen_formation = FormationHandler.choose_formation()

        SquadBuilder(chosen_formation, selected_players).save_squad_to_json(filename=f"Squad{nat_squad.squad_info.name}")
