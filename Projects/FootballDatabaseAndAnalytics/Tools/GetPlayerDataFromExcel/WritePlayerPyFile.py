import os
import textwrap
import uuid

from PlayerDefinitions.CareerInfo import CareerMode


class WritePlayerPyFileHandler:
    """ Class used to create .py files based on the output from ExcelSheetParser.get_all_sheet_info()
    """

    def __init__(self, output_location):
        self.output_location = output_location
        os.makedirs(self.output_location, exist_ok=True)  # Creates a folder if it is missing

    def generate_player_file(self, player_data_dict):
        """
        Function that takes output from ExcelSheetParser.get_all_sheet_info() and creates a .py file for the player
        :param player_data_dict: output dictionary from ExcelSheetParser.get_all_sheet_info()
        :return: None
        """

        first_name = player_data_dict["person_info"]["first_name"]
        last_name = player_data_dict["person_info"]["last_name"]

        import_content = self._generate_content_imports()
        person_info_content = self._generate_content_person_info(player_data_dict["person_info"])
        player_info_content = self._generate_content_player_info(player_data_dict["player_info"])
        physical_stats_content = self._generate_content_physical_stats(player_data_dict["physical_stats"])
        mental_stats_content = self._generate_content_mental_stats(player_data_dict["mental_stats"])
        technical_stats_content = self._generate_content_technical_stats(player_data_dict["technical_stats"])
        goalkeeping_stats_content = self._generate_content_goalkeeping_stats(player_data_dict["goalkeeping_stats"])
        ratings_content = self._generate_content_ratings()
        player_object_content = self._generate_content_player_object(first_name, last_name)



        # Construct the .py filename
        filename = f"{first_name}{last_name}.py"
        filepath = os.path.join(self.output_location, filename)

        # Combine all the content returns from each sub-function
        content = (import_content +
                   person_info_content +
                   player_info_content +
                   physical_stats_content +
                   mental_stats_content +
                   technical_stats_content +
                   goalkeeping_stats_content +
                   ratings_content +
                   player_object_content)

        # Write the content to the file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)


    @staticmethod
    def _generate_content_imports():
        """ Generates imports
        :return: string containing generated text
        """
        content = textwrap.dedent("""\
        from CountryDefinitions.Countries import Countries
        from PlayerDefinitions.CareerInfo import CareerMode
        from PlayerDefinitions.PlayerObject import Player, PlayerDefinitions, PersonInfo, PhysicalStats, MentalStats, TechnicalStats, GoalkeepingStats, PreferredFoot, Workrate, Traits
        from RatingCalculation import RatingCalculator
        """)
        return content

    @staticmethod
    def _generate_content_person_info(person_info):
        """ Generates the PersonInfo dataset
        :return: string containing generated text
        """
        # Person info
        first_name =    person_info["first_name"]
        last_name =     person_info["last_name"]
        nationality =   person_info["nationality"].upper()
        height =        person_info["height"]
        weight =        person_info["weight"]
        birthyear =     person_info["birthyear"]
        career_mode =   person_info["career_mode"]
        uuid_str =      uuid.uuid4()

        # Height calculations
        # Catch typo's in the Excel
        if height.endswith("'"):
            height = height[:-1] + '"'
        # Split by the '
        feet, inches = height.split("'")
        # Remove the double quotes
        feet = int(feet)
        inches = int(inches.replace('"', ''))
        # Build string that goes into the .py file
        height_dict_str = f'{{"feet": {feet}, "inches": {inches}}}'

        # Parse the lbs from the weight value
        weight = int(weight.replace("lbs", ""))

        # Get the name of the career mode by looping through the __dict__ function of the CareerMode class
        career_mode_name = None  # Default if not found
        # Loop through every attribute in the CareerMode class
        for name, obj in CareerMode.__dict__.items():
            # Check if the value (obj) is equal to the career_mode we got from ExcelTooling (defined in its function)
            if obj == career_mode:
                career_mode_name = name  # Store the attribute name (like "FIFA_21_SPARTA_ROTTERDAM")
                break

        content = f"""
person_info = PersonInfo(first_name=        "{first_name}",
                         last_name=         "{last_name}",
                         nationality=       Countries.{nationality},
                         height=            {height_dict_str},
                         weight=            {weight},
                         birthyear=         {birthyear},
                         career_mode=       CareerMode.{career_mode_name},
                         uuid=              "{uuid_str}",
                         )
"""
        return content

    @staticmethod
    def _generate_content_player_info(player_info):
        """ Generates the PlayerDefinitions dataset
        :return: string containing generated text
        """
        preferred_foot =        player_info["preferred_foot"].upper()
        weak_foot =             player_info["weak_foot"]
        skill_moves =           player_info["skill_moves"]
        att_work_rate =         player_info["att_work_rate"].upper()
        def_work_rate =         player_info["def_work_rate"].upper()
        traits =                []      # Default empty value
        kit_number =            None    # Default empty value

        content = f"""
player_info = PlayerDefinitions(preferred_foot=    PreferredFoot.{preferred_foot},
                         weak_foot=         {weak_foot},
                         skill_moves=       {skill_moves},
                         att_work_rate=     Workrate.{att_work_rate},
                         def_work_rate=     Workrate.{def_work_rate},
                         traits=            {traits},
                         kit_number=        {kit_number},
                         )
        """
        return content

    @staticmethod
    def _generate_content_physical_stats(physical_stats):
        """ Generates the PhysicalStats dataset
        :return: string containing generated text
        """
        acceleration =      physical_stats["acceleration"]
        agility =           physical_stats["agility"]
        balance =           physical_stats["balance"]
        jumping =           physical_stats["jumping"]
        reactions =         physical_stats["reactions"]
        sprint_speed =      physical_stats["sprint_speed"]
        stamina =           physical_stats["stamina"]
        strength =          physical_stats["strength"]

        content = f"""
physical_stats = PhysicalStats(acceleration=      {acceleration},
                               agility=           {agility},
                               balance=           {balance},
                               jumping=           {jumping},
                               reactions=         {reactions},
                               sprint_speed=      {sprint_speed},
                               stamina=           {stamina},
                               strength=          {strength},
                         )
        """
        return content

    @staticmethod
    def _generate_content_mental_stats(mental_stats):
        """ Generates the MentalStats dataset
        :return: string containing generated text
        """
        aggression =        mental_stats["aggression"]
        att_positioning =   mental_stats["att_positioning"]
        composure =         mental_stats["composure"]
        interceptions =     mental_stats["interceptions"]
        vision =            mental_stats["vision"]

        content = f"""
mental_stats = MentalStats(aggression=          {aggression},
                           att_positioning=     {att_positioning},
                           composure=           {composure},
                           interceptions=       {interceptions},
                           vision=              {vision},
                         )
        """
        return content

    @staticmethod
    def _generate_content_technical_stats(technical_stats):
        """ Generate the TechnicalStats dataset
        :return: string containing generated text
        """
        ball_control =          technical_stats["ball_control"]
        crossing =              technical_stats["crossing"]
        curve =                 technical_stats["curve"]
        def_awareness =         technical_stats["def_awareness"]
        dribbling =             technical_stats["dribbling"]
        fk_accuracy =           technical_stats["fk_accuracy"]
        finishing =             technical_stats["finishing"]
        heading_accuracy =      technical_stats["heading_accuracy"]
        long_pass =             technical_stats["long_pass"]
        long_shots =            technical_stats["long_shots"]
        penalties =             technical_stats["penalties"]
        short_pass =            technical_stats["short_pass"]
        shot_power =            technical_stats["shot_power"]
        slide_tackle =          technical_stats["slide_tackle"]
        stand_tackle =          technical_stats["stand_tackle"]
        volleys =                technical_stats["volleys"]

        content = f"""
technical_stats = TechnicalStats(ball_control=        {ball_control},
                                 crossing=            {crossing},
                                 curve=               {curve},
                                 def_awareness=       {def_awareness},
                                 dribbling=           {dribbling},
                                 fk_accuracy=         {fk_accuracy},
                                 finishing=           {finishing},
                                 heading_accuracy=    {heading_accuracy},
                                 long_pass=           {long_pass},
                                 long_shots=          {long_shots},
                                 penalties=           {penalties},
                                 short_pass=          {short_pass},
                                 shot_power=          {shot_power},
                                 slide_tackle=        {slide_tackle},
                                 stand_tackle=        {stand_tackle},
                                 volleys=             {volleys},
                                 )
                """
        return content

    @staticmethod
    def _generate_content_goalkeeping_stats(goalkeeping_stats):
        """ Generates the GoalkeepingStats dataset
        :return: string containing generated text
        """
        gk_diving =         goalkeeping_stats["gk_diving"]
        gk_handling =       goalkeeping_stats["gk_handling"]
        gk_kicking =        goalkeeping_stats["gk_kicking"]
        gk_positioning =    goalkeeping_stats["gk_positioning"]
        gk_reflexes =       goalkeeping_stats["gk_reflexes"]

        content = f"""
goalkeeping_stats = GoalkeepingStats(gk_diving=        {gk_diving},
                                     gk_handling=      {gk_handling},
                                     gk_kicking=       {gk_kicking},
                                     gk_positioning=   {gk_positioning},
                                     gk_reflexes=      {gk_reflexes},
                                     )
                        """
        return content

    @staticmethod
    def _generate_content_ratings():
        """ Generate the calculation of the ratings
        :return: string containing generated text
        """
        content = f"""
# Calculate the ratings from the stats
ratings = RatingCalculator(physical_stats=physical_stats, mental_stats=mental_stats, technical_stats=technical_stats,
                           goalkeeping_stats=goalkeeping_stats).get_ratings()
                """
        return content

    @staticmethod
    def _generate_content_player_object(first_name, last_name):
        """ Generate the PlayerObject definition
        :return: string containing generated text
        """
        first_name = first_name.upper()
        last_name = last_name.upper()

        content = f"""
# Create the player
{first_name}_{last_name} = Player(person_info=person_info, player_info=player_info, physical_stats=physical_stats,
                            mental_stats=mental_stats, technical_stats=technical_stats, goalkeeping_stats=goalkeeping_stats,
                            ratings=ratings)
                    """
        return content
