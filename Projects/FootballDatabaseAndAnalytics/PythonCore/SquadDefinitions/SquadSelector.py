from CareerModeData.PlayerList import PlayerList
from PlayerDefinitions.CareerInfo import Clubs, ClubObject


def group_players_per_nationality():
    """
    Function that groups the players per their nationality
    :return: dictionary containing each player per nationality, where the key is the nation and item a list of player(s)
    """

    grouped_players_per_nation_dict = {}

    for player in PlayerList.PLAYERS:
        nationality = player.person_info.nationality

        if nationality.name not in grouped_players_per_nation_dict.keys():
            grouped_players_per_nation_dict[nationality.name] = [player]
        elif nationality.name in grouped_players_per_nation_dict.keys():
            grouped_players_per_nation_dict[nationality.name].append(player)

    return grouped_players_per_nation_dict

class SquadInfo:
    """
    Generic class that handles information about a squad.
    This class is used to:
        - Manage information about the squad i.e. what is the team name, what region (UEFA, ...) etc.
        - Calculate the average rating of a Squad per discipline (ATT, MID, DEF).
    """
    def __init__(self, eligible_player_list):
        """
        Initialize the Squad info class
        :param eligible_player_list: List containing players which can be used to create a squad
        """
        self.eligible_player_list = eligible_player_list
        self.squad_info = None
        self.player_list = []

    def set_squad_info(self, club: ClubObject):
        """
        Sets squad information
        :param club: Clubs object
        :return: None
        """
        assert isinstance(club, ClubObject), f"Excepted ClubObject, got{type(club).__name__}"
        self.squad_info = club

    def get_player_count(self):
        return len(self.eligible_player_list)

    def validate_squad_depth(self, minimum_squad_depth=20):
        """
        Validate if the squad has enough depth to make a full squad
        :param minimum_squad_depth: Minimum required players (int)
        :return: Is minimum squad depth met? Boolean
        """
        if self.get_player_count() > minimum_squad_depth:
            return True
        else:
            return False

    def user_select_players(self, maximum_squad_depth=23):
        """
        Display all eligible players with their ratings per position in a readable table-like format.
        Players are sorted by their highest individual rating.
        For each player, positions are listed from the highest rating to lowest.
        :return List of selected players by user
        """

        available_player_list = []
        # Collect each player's ratings and sort them from best to worst position
        for player in self.eligible_player_list:
            ratings_list = self._get_player_best_positons(player)  # sorted list of (position, rating)
            available_player_list.append((player, ratings_list))

        # Sort players by their single highest rating, so the player with the highest positional rating is first
        available_player_list = self._get_sorted_player_list(available_player_list)

        # Add numeric IDs to each player tuple to be referenced by user input for removing players
        available_player_list_with_ids = [
            (idx + 1, player, ratings_list)
            for idx, (player, ratings_list) in enumerate(available_player_list)
        ]

        # Keep track of selected players
        selected_players = []

        # Initial display
        self._display_available_player_list(available_player_list_with_ids)

        while len(selected_players) < maximum_squad_depth and available_player_list_with_ids:
            user_input = input("\nEnter player number to select (or 'refresh' to update list): ").strip().lower()

            if user_input == "refresh":
                available_player_list_with_ids = self._refresh_player_list(
                    available_player_list_with_ids, selected_players
                )
                continue

            if not user_input.isdigit():
                print("❌ Please enter a valid number or 'refresh'.")
                continue

            selected_player_number = int(user_input)
            selected_player = self._get_player_by_id(available_player_list_with_ids, selected_player_number)

            if not selected_player:
                print("⚠️ No player found with that number. Try again.")
                continue

            if selected_player in selected_players:
                print("⚠️ That player has already been selected.")
                continue

            print(f"✅ You selected {selected_player.person_info.first_name} {selected_player.person_info.last_name}")
            selected_players.append(selected_player)

        # Final summary
        selected_players = self._display_final_selection(selected_players)

        return selected_players

    def _refresh_player_list(self, player_list_with_ids, selected_players):
        """
        Removes already selected players from the available list and reassigns IDs.
        Then redisplays the refreshed list.
        """
        updated_list = [
            (idx + 1, p, r)
            for idx, (i, p, r) in enumerate(player_list_with_ids)
            if p not in selected_players
        ]
        print("\nRefreshed player list:")
        if updated_list:
            # Assuming self context for display function
            # If moved to staticmethod, pass display function explicitly
            self._display_available_player_list(updated_list)
        else:
            print("(No players remaining.)")
        return updated_list

    @staticmethod
    def _get_player_by_id(player_list, player_id):
        """
        Finds and returns the player object corresponding to the given ID.
        Returns None if no match is found.
        """
        result = next((p for i, p, _ in player_list if i == player_id), None)
        return result

    @staticmethod
    def _display_available_player_list(player_list):
        """
        Function that displays the output of the sorted player lists (and ratings)
        :param player_list: Sorted player list and ratings from highest to low
        :return: None
        """
        # Determine max name length for alignment
        max_name_length = max(len(f"{p.person_info.first_name} {p.person_info.last_name}".strip())
                              for _, p, _ in player_list) + 10

        # Print text block for formatting
        print("\n=== AVAILABLE PLAYERS ===")
        print(f"{'ID':<4} {'NAME'.ljust(max_name_length)} RATINGS")
        print("-" * (max_name_length + 40))

        for player_id, player, ratings_list in player_list:
            full_name = f"{player.person_info.first_name} {player.person_info.last_name}".strip()
            name_formatted = full_name.ljust(max_name_length)
            ratings_str = ", ".join(f"{pos.upper():>3} {rating:>2}" for pos, rating in ratings_list)

            print(f"{player_id:<4} {name_formatted}: {ratings_str}")

    @staticmethod
    def _display_final_selection(selected_players):
        """
        Prints a final summary table of all selected players with IDs and sorted ratings.
        :return: a list of dicts so the same data can be accessed programmatically:
            "id": player id
            "player": information about the player
            "name": player full name
            "ratings": the ratings sorted from highest to lowest in a list containing tuples
            "ratings_str": ratings as they are printed by the display function

        """
        if not selected_players:
            print("\n(No players were selected.)")
            return []

        print("\n=== FINAL SELECTED PLAYERS ===")
        print(f"{'ID':<4} {'NAME':<25} RATINGS")
        print("-" * 70)

        # Store the display data in a list so it can be accessed elsewhere
        display_data = []

        for idx, player in enumerate(selected_players, 1):
            full_name = f"{player.person_info.first_name} {player.person_info.last_name}".strip()
            sorted_ratings = sorted(vars(player.ratings).items(), key=lambda x: x[1], reverse=True)
            ratings_str = ", ".join(f"{pos.upper()} {rating}" for pos, rating in sorted_ratings)

            print(f"{idx:<4} {full_name:<25} {ratings_str}")

            # Add structured info for reuse
            display_data.append({
                "id": idx,
                "player": player,
                "name": full_name,
                "ratings": sorted_ratings,
                "ratings_str": ratings_str
            })

        return display_data

    @staticmethod
    def _get_sorted_player_list(player_list):
        """
        Sort players by their single highest rating, so the player with the highest positional rating is first
        :param player_list: Player list of tuples where the second value are ratings with the best position first
        :return: Sorted list where the player with the highest rating is first
        """
        player_list.sort(
            key=lambda player_tuple: player_tuple[1][0][1],  # highest rating is first in sorted ratings_list
            reverse=True
        )
        return player_list

    @staticmethod
    def _get_player_best_positons(player_object):
        """
        Sorts the player ratings based on highest to lowest value by converting the dataset to a
        dictionary and then to a list of tuples.
        :param player_object: PlayerObject where the ratings are acquired from
        :return: List containing the ratings per position from the highest value to lowest
        """
        sorted_ratings = sorted(vars(player_object.ratings).items(), key=lambda x:x[1], reverse=True)
        return sorted_ratings

class NationalSquadInfo(SquadInfo):
    """
    Subclass of the SquadInfo for handling national team specific variations
    """
    def set_squad_info(self, club=None):
        """
        Set the squad info based on the nationality of the player
        :param club: set to None, as this value is not used in this subclass
        :return: None
        """
        for player in self.eligible_player_list:
            country = player.person_info.nationality
            country_name = country.name
            uuid = country.uuid
            self.squad_info = ClubObject(name=country_name, country=country, uuid=uuid)
            break

    # todo function that calculates the average rating of a squad per squad group (att, mid, def)
    # todo function that writes the selected team to a file to be stored
