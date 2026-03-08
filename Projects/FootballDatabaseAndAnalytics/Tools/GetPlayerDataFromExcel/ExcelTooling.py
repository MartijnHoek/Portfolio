import pandas


class ExcelFileHandler:
    """ Class used loading in the complete Excel file and retrieving the sheet names to be used by ExcelSheetParser
    """

    def __init__(self, input_file):
        self.excel_file = pandas.ExcelFile(input_file)

    def get_sheet_names(self):
        """ Function used to get the Excel sheet names from the file in a list,
        and removing the 'Overview' page from this list.
        Returns the list
        """
        sheet_name_list = self.excel_file.sheet_names

        if "Overview" in sheet_name_list:
            sheet_name_list.remove("Overview")
        return sheet_name_list

class ExcelSheetParser:
    """ Class used for reading player data from the Excel files and converting them to dictionaries as output
    """
    def __init__(self, input_file, sheet_name, career_mode=None):
        self.data_frame = pandas.read_excel(input_file, sheet_name)
        self.career_mode = career_mode

    def get_all_sheet_info(self):
        sheet_info_dict = {
            "person_info":          self.get_person_info(),
            "player_info":          self.get_player_info(),
            "physical_stats":       self.get_physical_stats(),
            "mental_stats":         self.get_mental_stats(),
            "technical_stats":      self.get_technical_stats(),
            "goalkeeping_stats":    self.get_goalkeeping_stats(),
        }
        return sheet_info_dict

    def get_person_info(self):
        first_name =    self.data_frame.iloc[0, 2]
        last_name =     self.data_frame.iloc[1, 2]
        nationality =   self.data_frame.iloc[2, 2]
        height =        self.data_frame.iloc[3, 2]
        weight =        self.data_frame.iloc[4, 2]
        birthyear =     self.data_frame.iloc[5, 2]
        career_mode =   self.career_mode

        person_info_dict = {
            "first_name":   first_name,
            "last_name":    last_name,
            "nationality":  nationality,
            "height":       height,
            "weight":       weight,
            "birthyear":    birthyear,
            "career_mode":  career_mode,
        }
        return person_info_dict

    def get_player_info(self):
        preferred_foot =    self.data_frame.iloc[10, 2]
        weak_foot =         self.data_frame.iloc[11, 2]
        skill_moves =       self.data_frame.iloc[12, 2]
        att_work_rate =     self.data_frame.iloc[13, 2]
        def_work_rate =     self.data_frame.iloc[14, 2]

        player_info_dict = {
            "preferred_foot":   preferred_foot,
            "weak_foot":        weak_foot,
            "skill_moves":      skill_moves,
            "att_work_rate":    att_work_rate,
            "def_work_rate":    def_work_rate,
        }
        return player_info_dict

    def get_physical_stats(self):
        acceleration = self.data_frame.iloc[1, 5]
        agility = self.data_frame.iloc[2, 5]
        balance = self.data_frame.iloc[3, 5]
        jumping = self.data_frame.iloc[4, 5]
        reactions = self.data_frame.iloc[5, 5]
        sprint_speed = self.data_frame.iloc[6, 5]
        stamina = self.data_frame.iloc[7, 5]
        strength = self.data_frame.iloc[8, 5]

        physical_stats_dict = {
            "acceleration":    acceleration,
            "agility":         agility,
            "balance":         balance,
            "jumping":         jumping,
            "reactions":       reactions,
            "sprint_speed":    sprint_speed,
            "stamina":         stamina,
            "strength":        strength,
        }
        return physical_stats_dict

    def get_mental_stats(self):
        aggression = self.data_frame.iloc[1, 8]
        att_positioning = self.data_frame.iloc[2, 8]
        composure = self.data_frame.iloc[3, 8]
        interceptions = self.data_frame.iloc[4, 8]
        vision = self.data_frame.iloc[5, 8]

        mental_stats_dict = {
            "aggression":           aggression,
            "att_positioning":      att_positioning,
            "composure":            composure,
            "interceptions":        interceptions,
            "vision":               vision,
        }
        return mental_stats_dict

    def get_technical_stats(self):
        ball_control = self.data_frame.iloc[1, 11]
        crossing = self.data_frame.iloc[2, 11]
        curve = self.data_frame.iloc[3, 11]
        def_awareness = self.data_frame.iloc[4, 11]
        dribbling = self.data_frame.iloc[5, 11]
        fk_accuracy = self.data_frame.iloc[6, 11]
        finishing = self.data_frame.iloc[7, 11]
        heading_accuracy = self.data_frame.iloc[8, 11]
        long_pass = self.data_frame.iloc[9, 11]
        long_shots = self.data_frame.iloc[10, 11]
        penalties = self.data_frame.iloc[11, 11]
        short_pass = self.data_frame.iloc[12, 11]
        shot_power = self.data_frame.iloc[13, 11]
        slide_tackle = self.data_frame.iloc[14, 11]
        stand_tackle = self.data_frame.iloc[15, 11]
        volleys = self.data_frame.iloc[16, 11]

        technical_stats_dict = {
            "ball_control":         ball_control,
            "crossing":             crossing,
            "curve":                curve,
            "def_awareness":        def_awareness,
            "dribbling":            dribbling,
            "fk_accuracy":          fk_accuracy,
            "finishing":            finishing,
            "heading_accuracy":     heading_accuracy,
            "long_pass":            long_pass,
            "long_shots":           long_shots,
            "penalties":            penalties,
            "short_pass":           short_pass,
            "shot_power":           shot_power,
            "slide_tackle":         slide_tackle,
            "stand_tackle":         stand_tackle,
            "volleys":              volleys,
        }
        return technical_stats_dict

    def get_goalkeeping_stats(self):
        gk_diving = self.data_frame.iloc[1, 14]
        gk_handling = self.data_frame.iloc[2, 14]
        gk_kicking = self.data_frame.iloc[3, 14]
        gk_positioning = self.data_frame.iloc[4, 14]
        gk_reflexes = self.data_frame.iloc[5, 14]

        goalkeeping_stats_dict = {
            "gk_diving":        gk_diving,
            "gk_handling":      gk_handling,
            "gk_kicking":       gk_kicking,
            "gk_positioning":   gk_positioning,
            "gk_reflexes":      gk_reflexes,
        }
        return goalkeeping_stats_dict
