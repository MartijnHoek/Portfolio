class FormationObject(object):
    """
    Object that is used to define formations, entered values are the amount of players per this position (gk is excluded as always 1)
    """
    def __init__(self, name,
                 lb_count=0, rb_count=0, cb_count=0,
                 cdm_count=0, cm_count=0, cam_count=0,
                 lm_count=0, rm_count=0,
                 lw_count=0, rw_count=0,
                 st_count=0):

        self.name = name
        self.lb_count = lb_count
        self.rb_count = rb_count
        self.cb_count = cb_count
        self.cdm_count = cdm_count
        self.cm_count = cm_count
        self.cam_count = cam_count
        self.lm_count = lm_count
        self.rm_count = rm_count
        self.lw_count = lw_count
        self.rw_count = rw_count
        self.st_count = st_count

        self.amount_defenders = self.lb_count + self.rb_count + self.cb_count
        self.amount_midfielders = self.cdm_count + self.cm_count + self.cam_count + self.lm_count + self.rm_count
        self.amount_attackers = self.lw_count + self.rw_count + self.st_count

        self.required_positions = {}

        self._fill_required_positions()

    def _fill_required_positions(self):
        """ Count how many times a position was defined for a formation so that self.required_positions get filled """
        self.required_positions["gk"] = 1
        positions = [
            "lb", "rb", "cb",
            "cdm", "cm", "cam", "lm", "rm",
            "lw", "rw", "st"
        ]

        for pos in positions:
            count = getattr(self, f"{pos}_count", 0)
            if count:
                self.required_positions[pos] = count

    def __repr__(self):
        """ Defined represent to make object easier to read
        :return: Print formation info as FormationObject(name=4-3-3 Defensive, required_positions={gk: 1, ....}
        """
        return f"FormationObject(name={self.name!r}, required_positions={self.required_positions})"


class Formations:
    # 3 at the back
    FORMATION_3_1_4_2 =                 FormationObject("3-1-4-2", cb_count=3, cdm_count=1, cm_count=2, lm_count=1, rm_count=1, st_count=2)
    FORMATION_3_4_1_2 =                 FormationObject("3-4-1-2", cb_count=3, cm_count=2, cam_count=1, lm_count=1, rm_count=1, st_count=2)
    FORMATION_3_4_2_1 =                 FormationObject("3-4-2-1", cb_count=3, cm_count=2, cam_count=2, lm_count=1, rm_count=1, st_count=1)
    FORMATION_3_5_2 =                   FormationObject("3-5-2", cb_count=3, cdm_count=2, cam_count=1, lm_count=1, rm_count=1, st_count=2)
    FORMATION_3_4_3 =                   FormationObject("3-4-3", cb_count=3, cm_count=2, lm_count=1, rm_count=1, lw_count=1, rw_count=1, st_count=2)

    # 4 at the back - 2 midfielders
    FORMATION_4_2_4 =                   FormationObject("4-2-4", lb_count=1, rb_count=1, cb_count=2, cm_count=2, lw_count=1, rw_count=1, st_count=2)

    # 4 at the back - 3 midfielders
    FORMATION_4_3_3 =                   FormationObject("4-3-3", lb_count=1, rb_count=1, cb_count=2, cm_count=3, lw_count=1, rw_count=1, st_count=1)
    FORMATION_4_3_3_ATT =               FormationObject("4-3-3 Attacking", lb_count=1, rb_count=1, cb_count=2, cm_count=2, cam_count=1, lw_count=1, rw_count=1, st_count=1)
    FORMATION_4_3_3_DEF =               FormationObject("4-3-3 Defensive", lb_count=1, rb_count=1, cb_count=2, cm_count=2, cdm_count=1, lw_count=1, rw_count=1, st_count=1)
    FORMATION_4_3_3_ULTRA_DEF =         FormationObject("4-3-3 Ultra Defensive", lb_count=1, rb_count=1, cb_count=2, cm_count=1, cdm_count=2, lw_count=1, rw_count=1, st_count=1)

    FORMATION_4_2_1_3 =                 FormationObject("4-1-2-3", lb_count=1, rb_count=1, cb_count=2, cdm_count=2, cam_count=1, lw_count=1, rw_count=1, st_count=1)

    # 4 at the back - 4 midfielders
    FORMATION_4_4_2 =                   FormationObject("4-4-2", lb_count=1, rb_count=1, cb_count=2, cm_count=2, lm_count=1, rm_count=1, st_count=2)
    FORMATION_4_4_2_DEFENSIVE =         FormationObject("4-4-2 Defensive", lb_count=1, rb_count=1, cb_count=2, cdm_count=2, lm_count=1, rm_count=1, st_count=2)

    FORMATION_4_1_2_1_2 =               FormationObject("4-1-2-1-2", lb_count=1, rb_count=1, cb_count=2, cdm_count=1, cam_count=1, lm_count=1, rm_count=1, st_count=2)
    FORMATION_4_1_2_1_2_COMPACT =       FormationObject("4-1-2-1-2 Compact", lb_count=1, rb_count=1, cb_count=2, cdm_count=1, cam_count=1, cm_count=2, st_count=2)

    FORMATION_4_3_1_2 =                 FormationObject("4-3-1-2", lb_count=1, rb_count=1, cb_count=2, cam_count=1, cm_count=3, st_count=2)

    FORMATION_4_1_3_2 =                 FormationObject("4-1-3-2", lb_count=1, rb_count=1, cb_count=2, cdm_count=1, cm_count=1, lm_count=1, rm_count=1, st_count=2)

    FORMATION_4_2_2_2 =                 FormationObject("4-2-2-2", lb_count=1, rb_count=1, cb_count=2, cdm_count=2, cam_count=2, st_count=2)

    # 4 at the back - 5 midfielders
    FORMATION_4_5_1 =                   FormationObject("4-5-1", lb_count=1, rb_count=1, cb_count=2, cm_count=1, cam_count=2, lm_count=1, rm_count=1, st_count=1)
    FORMATION_4_5_1_ATTACKING =         FormationObject("4-5-1 Attacking", lb_count=1, rb_count=1, cb_count=2, cm_count=3, lm_count=1, rm_count=1, st_count=1)

    FORMATION_4_1_4_1 =                 FormationObject("4-1-4-1", lb_count=1, rb_count=1, cb_count=2, cdm_count=1, cm_count=2, lm_count=1, rm_count=1, st_count=1)

    FORMATION_4_2_3_1 =                 FormationObject("4-2-3-1", lb_count=1, rb_count=1, cb_count=2, cdm_count=2, cam_count=1, lm_count=1, rm_count=1, st_count=1)
    FORMATION_4_2_3_1_COMPACT =         FormationObject("4-2-3-1 Compact", lb_count=1, rb_count=1, cb_count=2, cdm_count=2, cam_count=3, st_count=1)

    FORMATION_4_3_2_1 =                 FormationObject("4-3-2-1", lb_count=1, rb_count=1, cb_count=2, cam_count=2, cm_count=3, st_count=1)

    FORMATION_4_4_1_1 =                 FormationObject("4-4-1-1", lb_count=1, rb_count=1, cb_count=2, cam_count=1, cm_count=2, lm_count=1, rm_count=1, st_count=1)

    # 5 at the back
    FORMATION_5_2_1_2 =                 FormationObject("5-2-1-2", lb_count=1, rb_count=1, cb_count=3, cm_count=2, cam_count=1, st_count=2)
    FORMATION_5_2_3 =                   FormationObject("5-2-3", lb_count=1, rb_count=1, cb_count=3, cm_count=2, lw_count=1, rw_count=1, st_count=1)
    FORMATION_5_3_2 =                   FormationObject("5-3-2", lb_count=1, rb_count=1, cb_count=3, cdm_count=1, cm_count=2, st_count=2)
    FORMATION_5_4_1 =                   FormationObject("5-4-1", lb_count=1, rb_count=1, cb_count=3, cm_count=2, lm_count=1, rm_count=1, st_count=1)


def choose_formation():
    """Function that cycles to all defined values"""
    # Collect all formations from the class
    formations = [
        (name, value)
        for name, value in Formations.__dict__.items()
        if isinstance(value, FormationObject)
    ]

    # Sort by the formation's display name (e.g. "3-4-1-2")
    formations.sort(key=lambda item: item[1].name)

    # Compute the longest name for nice alignment
    longest_name = max(len(f.name) for _, f in formations)

    print("Available formations:\n")
    for i, (name, formation) in enumerate(formations, start=1):
        # Gather all position counts dynamically
        positions = [
            f"{attr.replace('_count', '').upper()}×{count}"
            for attr, count in vars(formation).items()
            if attr.endswith("_count") and count > 0
        ]
        position_summary = ", ".join(positions)

        # Print in columns (number, name, positions)
        print(f"{i:>2}. {formation.name:<{longest_name}} | {position_summary}")

    # Handle user input safely
    while True:
        try:
            choice = int(input("\nEnter the number of your chosen formation: "))
            if 1 <= choice <= len(formations):
                chosen_name, chosen_formation = formations[choice - 1]
                print(f"\nYou selected: {chosen_formation.name}")
                return chosen_formation
            else:
                print(f"Please enter a number between 1 and {len(formations)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
