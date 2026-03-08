from CountryDefinitions.Countries import Countries
from PlayerDefinitions.CareerInfo import CareerMode
from PlayerDefinitions.PlayerObject import Player, PlayerInfo, PersonInfo, PhysicalStats, MentalStats, TechnicalStats, GoalkeepingStats, PreferredFoot, Workrate, Traits
from PlayerDefinitions.RatingCalculation import RatingCalculator

person_info = PersonInfo(first_name=        "David",
                         last_name=         "Villa",
                         nationality=       Countries.SPAIN,
                         height=            {"feet": 5, "inches": 9},
                         weight=            152,
                         birthyear=         1981,
                         career_mode=       CareerMode.FIFA_12_JUVENTUS,
                         uuid=              "5b3d7674-4f56-4354-8ee1-7be1392378cc",
                         )

player_info = PlayerInfo(preferred_foot=    PreferredFoot.RIGHT,
                         weak_foot=         5,
                         skill_moves=       4,
                         att_work_rate=     Workrate.HIGH,
                         def_work_rate=     Workrate.MEDIUM,
                         traits=            [Traits.FINESSE_SHOT],
                         kit_number=        7,
                         )
        
physical_stats = PhysicalStats(acceleration=      87,
                               agility=           81,
                               balance=           75,
                               jumping=           69,
                               reactions=         90,
                               sprint_speed=      84,
                               stamina=           73,
                               strength=          70,
                         )
        
mental_stats = MentalStats(aggression=          71,
                           att_positioning=     88,
                           composure=           88,
                           interceptions=       29,
                           vision=              80,
                         )
        
technical_stats = TechnicalStats(ball_control=        89,
                                 crossing=            79,
                                 curve=               82,
                                 def_awareness=       22,
                                 dribbling=           86,
                                 fk_accuracy=         85,
                                 finishing=           93,
                                 heading_accuracy=    77,
                                 long_pass=           60,
                                 long_shots=          88,
                                 penalties=           92,
                                 short_pass=          83,
                                 shot_power=          90,
                                 slide_tackle=        38,
                                 stand_tackle=        28,
                                 volleys=             87,
                                 )
                
goalkeeping_stats = GoalkeepingStats(gk_diving=        8,
                                     gk_handling=      9,
                                     gk_kicking=       9,
                                     gk_positioning=   11,
                                     gk_reflexes=      9,
                                     )
                        
# Calculate the ratings from the stats
ratings = RatingCalculator(physical_stats=physical_stats, mental_stats=mental_stats, technical_stats=technical_stats,
                           goalkeeping_stats=goalkeeping_stats).get_ratings()
                
# Create the player
DAVID_VILLA = Player(person_info=person_info, player_info=player_info, physical_stats=physical_stats,
                            mental_stats=mental_stats, technical_stats=technical_stats, goalkeeping_stats=goalkeeping_stats,
                            ratings=ratings)
                    