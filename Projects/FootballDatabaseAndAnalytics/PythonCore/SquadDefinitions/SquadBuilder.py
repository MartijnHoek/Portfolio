import json


class SquadBuilder:
    def __init__(self, formation, squad):
        self.formation = formation
        self.squad = squad
        self.filled_formation = {}

        print(f"\nBuilding squad for formation: {formation.name}\n")

        # Loop through all required positions
        for position, amount in formation.required_positions.items():
            for i in range(amount):
                pos_label = f"{position.upper()} #{i+1}" if amount > 1 else position.upper()
                self.select_player_for_position(pos_label)

        print("\n✅ Squad completed!\n")
        self.show_final_squad()

    def select_player_for_position(self, position_label):
        """Let user choose a player for one position"""
        while True:
            available_players = [
                p for p in self.squad if p["id"] not in [pl["id"] for pl in self.filled_formation.values()]
            ]

            print(f"\nAvailable players for {position_label}:")
            print(f"{'ID':<4} {'Name':<20} | Ratings")
            print("-" * 50)
            for player in available_players:
                ratings_str = player.get("ratings_str", "N/A")
                print(f"{player['id']:<4} {player['name']:<20} | {ratings_str}")

            choice = input(f"\nEnter player ID for {position_label} (or 'r' to review current squad): ").strip()

            if choice.lower() == "r":
                self.show_current_squad()
                continue

            try:
                player_id = int(choice)
                selected = next((p for p in available_players if p["id"] == player_id), None)
                if not selected:
                    print("❌ Invalid ID. Please try again.")
                    continue

                # Confirm
                confirm = input(f"Confirm {selected['name']} as {position_label}? (y/n): ").lower()
                if confirm == "y":
                    self.filled_formation[position_label] = selected
                    print(f"✅ {selected['name']} locked in as {position_label}.")
                    break
                else:
                    print("↩️  Selection canceled.")
            except ValueError:
                print("❌ Please enter a valid number or 'r'.")

    def show_current_squad(self):
        """Show what’s been selected so far"""
        print("\n Current Squad:")
        if not self.filled_formation:
            print("  (no players selected yet)")
        else:
            for pos, player in self.filled_formation.items():
                print(f"  {pos:<10} → {player['name']} ({player.get('ratings_str', 'N/A')})")
        print()

    def show_final_squad(self):
        """Show final formation"""
        print("Final Squad:")
        for pos, player in self.filled_formation.items():
            print(f"  {pos:<10} → {player['name']} ({player.get('ratings_str', 'N/A')})")

    def save_squad_to_json(self, filename=None):
        """Save the final squad to a JSON file, showing positional ratings and a bench list."""
        if filename is None:
            filename = f"DefinedTeams/squad_{self.formation.name.lower().replace(' ', '_')}.json"
        else:
            filename = f'DefinedTeams/{filename}.json'


        # Convert position label like "CB #1" → "cb"
        def normalize_position(pos_label):
            return pos_label.split()[0].lower()

        # Build positions section
        positions_data = {}
        for pos_label, player in self.filled_formation.items():
            pos_key = normalize_position(pos_label)

            # Extract player's rating for this specific position (if available)
            rating_list = player.get("ratings", [])
            if isinstance(rating_list, dict):
                # Convert dict {pos: val} → list of tuples
                rating_list = list(rating_list.items())

            rating_for_pos = next(
                (r for p, r in rating_list if p.lower() == pos_key), None
            )

            positions_data[pos_label] = {
                "id": player["id"],
                "name": player["name"],
                "position": pos_key,
                "rating_for_position": rating_for_pos,
            }

        # --- Create bench list ---
        selected_ids = {p["id"] for p in self.filled_formation.values()}
        remaining_players = [p for p in self.squad if p["id"] not in selected_ids]

        bench = []
        for p in remaining_players:
            ratings = p.get("ratings", [])
            if isinstance(ratings, dict):
                ratings = list(ratings.items())
            # Find the highest rating
            best_pos, best_rating = max(ratings, key=lambda x: x[1])
            bench.append({
                "id": p["id"],
                "name": p["name"],
                "best_position": best_pos,
                "best_rating": best_rating
            })

        # Sort bench from highest to lowest rating
        bench.sort(key=lambda x: x["best_rating"], reverse=True)

        # --- Final structure ---
        squad_data = {
            "formation": self.formation.name,
            "positions": positions_data,
            "bench": bench
        }

        # --- Save to JSON ---
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(squad_data, f, ensure_ascii=False, indent=4)

        print(f"\nSquad saved to '{filename}' successfully.\n")
