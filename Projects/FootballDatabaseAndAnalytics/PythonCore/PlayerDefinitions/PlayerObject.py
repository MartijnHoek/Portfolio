from dataclasses import dataclass
from typing import Optional

from CountryDefinitions.GeographicObjects import Country
from PlayerDefinitions.CareerInfo import CareerObject
from PlayerDefinitions.RatingCalculation import PositionRatings


@dataclass
class PersonInfo:
    """ Dataset defining all the data for personal information """
    first_name:     str
    last_name:      str
    nationality:    Country
    height:         dict
    weight:         int
    birthyear:      int
    career_mode:    CareerObject
    uuid:           str

@dataclass
class PlayerInfo:
    """ Dataset defining all the data for more player football-oriented information """
    preferred_foot: str
    weak_foot:      int
    skill_moves:    int
    att_work_rate:  str
    def_work_rate:  str
    traits:         list
    kit_number:     Optional[int] = None

@dataclass
class PhysicalStats:
    """ Dataset defining all the physical values of a player """
    acceleration:   int
    agility:        int
    balance:        int
    jumping:        int
    reactions:      int
    sprint_speed:   int
    stamina:        int
    strength:       int

@dataclass
class MentalStats:
    """ Dataset defining all the mental values of a player """
    aggression:         int
    att_positioning:    int
    composure:          int
    interceptions:      int
    vision:             int

@dataclass
class TechnicalStats:
    """ Dataset defining all the technical values of a player """
    ball_control:       int
    crossing:           int
    curve:              int
    def_awareness:      int
    dribbling:          int
    fk_accuracy:        int
    finishing:          int
    heading_accuracy:   int
    long_pass:          int
    long_shots:         int
    penalties:          int
    short_pass:         int
    shot_power:         int
    slide_tackle:       int
    stand_tackle:       int
    volleys:            int

@dataclass
class GoalkeepingStats:
    """ Dataset defining all the goalkeeping values of a player """
    gk_diving:          int
    gk_handling:        int
    gk_kicking:         int
    gk_positioning:     int
    gk_reflexes:        int

@dataclass
class Player:
    """ Combining all the datasets into one big dataset that is a player """
    person_info:        PersonInfo
    player_info:        PlayerInfo
    physical_stats:     PhysicalStats
    mental_stats:       MentalStats
    technical_stats:    TechnicalStats
    goalkeeping_stats:  GoalkeepingStats
    ratings:            PositionRatings

class PreferredFoot:
    """ Class used to define which foot a player prefers """
    RIGHT = "Right"
    LEFT =  "Left"

class Workrate:
    """ Class used to define which workrate a player has (attacking and defending)"""
    LOW =           "LOW"
    MEDIUM =        "MEDIUM"
    HIGH =          "HIGH"
    NOT_AVAILABLE = "NOT AVAILABLE"

@dataclass
class TraitInfo:
    """ Dataset used to define the trait info"""
    name:   str     # Name of the Trait
    uuid:   str     # Unique Identifier

class Traits:
    """ Class used for defining all the different traits """
    # Passing
    LONG_PASSER                 = TraitInfo("Long Passer", "688aa2ef-0f1f-4798-94bb-7403781df23a")
    PLAYMAKER                   = TraitInfo("Playmaker", "4c1349c6-5912-4ce9-af17-a8e8331dd861")
    INCISIVE_PASS               = TraitInfo("Incisive Pass", "e2420b2d-55a5-46e1-8ee0-1258f145cdc2")
    TIKI_TAKA                   = TraitInfo("Tiki Taka", "75752a2f-0b6e-461d-985f-3783dae6d4a6")
    PINGED_PASS                 = TraitInfo("Pinged Pass", "6a8fe17c-68b6-4540-82bf-44441d55ffce")
    LONG_BALL_PASS              = TraitInfo("Long Ball Pass", "c8c21445-74c7-481f-8ae5-65c6779ff45c")
    LONG_BALL_PASS_PLUS         = TraitInfo("Long Ball Pass +", "559ed7cd-d5f6-4938-9318-9124271bad60")
    WHIPPED_PASS                = TraitInfo("Whipped Pass", "61897ce3-475a-4de4-87a5-a74fbc49b0b5")
    EARLY_CROSSER               = TraitInfo("Early Crosser", "55aed322-581e-4945-a8aa-158e154134ce")

    # Shooting
    FINESSE_SHOT                = TraitInfo("Finesse Shot", "42e59596-e351-4121-9a99-7f8a2a8fc808")
    OUTSIDE_FOOT_SHOT           = TraitInfo("Outside Foot Shot", "d8f6c108-6d58-44a1-8c42-70e5c5a6301b")
    CHIP_SHOT                   = TraitInfo("Chip Shot", "ac5923a4-8169-4bbf-9e1a-fb1cb7215c83")
    LONG_SHOT_TAKER             = TraitInfo("Long Shot Taker", "14ff7d2e-fcff-4590-b7d7-32e64569e6bb")
    POWER_SHOT                  = TraitInfo("Power Shot", "90c63449-122b-4b81-8021-c0a5e05523c2")

    # Throw in
    GIANT_THROW_IN              = TraitInfo("Giant Throw-in", "9298d910-75ff-4bc5-8dff-60095b25fc1d")
    LONG_THROW                  = TraitInfo("Long Throw", "c7855a1e-7244-44bc-bbcb-28ce66568a8c")
    LONG_THROW_IN               = TraitInfo("Long Throw-in", "54e9d440-2740-4052-bade-130d2c732c9c")

    # Stamina
    SECOND_WIND                 = TraitInfo("Second Wind", "315b4612-d1f9-47af-b50d-d14f60a13d76")
    RELENTLESS                  = TraitInfo("Relentless", "130f432c-3091-4bd9-830c-052fed23bfe6")

    # Injury
    SOLID_PLAYER                = TraitInfo("Solid Player", "ed991f75-876a-4734-8fec-e7261db815af")
    INJURY_PRONE                = TraitInfo("Injury Prone", "d605a42f-41b1-4a47-a155-ae845ea5e565")

    # Skills
    FLAIR                       = TraitInfo("Flair", "b8db9e1d-bbb8-44a4-8ed7-45d6ffff7d68")
    TRIVELA                     = TraitInfo("Trivela", "f783876e-9566-4f19-9750-2177d7dd8961")
    TRICKSTER                   = TraitInfo("Trickster", "50fc880f-99b4-4f70-adbf-8abf5d6fb28e")
    ACROBATIC                   = TraitInfo("Acrobatic", "f6250d8c-5fcc-4104-9747-871dddbe3a8a")

    # Dribbling
    TECHNICAL_DRIBBLER          = TraitInfo("Technical Dribbler", "ab0aa283-ae88-49f6-b18a-9db5d9dea02a")
    SPEED_DRIBBLER              = TraitInfo("Speed Dribbler", "816e9666-edff-41c9-9d55-77a659bfd01b")
    TECHNICAL                   = TraitInfo("Technical", "b5164e7c-0b9a-42db-ada8-41a3c6c7600d")
    RAPID                       = TraitInfo("Rapid", "c2de80b9-046f-4d90-8981-500d82755962")
    SKILLED_DRIBBLING           = TraitInfo("Skilled Dribbling", "4b19a3f4-9fb4-4182-8ff9-6a57ff97d79f")

    # Defending
    DIVES_INTO_TACKLES          = TraitInfo("Dives Into Tackles", "4235b13c-679d-4cd8-b156-aee1b0bb6213")
    JOCKEY                      = TraitInfo("Jockey", "cd3f7e53-5913-41b0-8b26-79b065912d50")
    INTERCEPT                   = TraitInfo("Intercept", "2a1ec346-2462-40b5-a561-d24facd61d46")
    SLIDE_TACKLE                = TraitInfo("Slide Tackle", "31f20da4-1794-4bb3-ae05-deb572713d8e")
    ANTICIPATE                  = TraitInfo("Anticipate", "ef48834f-9162-458c-9bbd-de2a9ee2499d")
    BLOCK                       = TraitInfo("Block", "1df8df96-97bd-4666-934f-6fb734a5420f")

    # Goalkeeping
    RUSHES_OUT_OF_GOAL          = TraitInfo("Rushes Out Of Goal", "8fc32532-bbe8-488d-adb5-5896dc53d086")
    COMES_FOR_CROSSES           = TraitInfo("Comes For Crosses", "c4dc272e-397e-440f-963e-f45f1d9bc071")
    SAVES_WITH_FEET             = TraitInfo("Saves With Feet", "a71361e2-055f-42fa-be2a-343c7ce2de6f")
    RUSH_OUT                    = TraitInfo("Rush Out", "f2c3857f-ac85-47dc-8892-95b0c7443192")
    RUSH_OUT_PLUS               = TraitInfo("Rush Out +", "f90c27b0-57c6-41b0-9197-7e3cb0abe03c")
    FOOTWORK                    = TraitInfo("Footwork", "22253222-5692-4427-b521-74ea48dff0e1")
    CROSS_CLAIMER               = TraitInfo("Cross Claimer", "517dac19-d613-4487-b25e-378880c39f32")
    FAR_THROW                   = TraitInfo("Far Throw", "1634185e-6a5e-46c3-92de-95a4b724e2d3")
    GK_LONG_THROW               = TraitInfo("GK Long Throw", "cf5d0463-ac05-42c5-9c9b-3441c3a7f5ce")
    GK_UP_FOR_CORNERS           = TraitInfo("GK Up For Corners", "f78c3119-f8bb-476f-87b2-5976e3586158")

    # Captaincy
    TEAM_PLAYER                 = TraitInfo("Team Player", "a3d6696a-b3b8-48b4-818c-fc95ffda24bf")
    LEADERSHIP                  = TraitInfo("Leadership", "e23774af-99f4-4c30-a95a-47ea50d0a338")
    ONE_CLUB_PLAYER             = TraitInfo("One Club Player", "e8179f79-b640-4c4b-898a-5e270397be8d")

    # Heading
    POWER_HEADER                = TraitInfo("Power Header", "81446da8-021a-4e1f-8c5c-71b007a6433c")
    AERIAL                      = TraitInfo("Aerial", "e53c3b63-b9c5-42ab-a409-8114a159aadb")

    # Set Pieces
    DEAD_BALL                   = TraitInfo("Dead Ball", "54f85922-2397-4f88-b4e4-4e3259c01841")
    POWER_FREE_KICK             = TraitInfo("Power Free-kick", "1d681c1a-c8e4-4c8a-9fd7-374a87f29263")
    CORNER_SPECIALIST           = TraitInfo("Corner Specialist", "83097e13-6e9f-40bc-b718-faf6de0eb644")
    TAKES_FINESSE_FREE_KICKS    = TraitInfo("Takes Finesse Free Kicks", "6b157def-baaf-4692-a50e-f14a77bf8e8a")
    STUTTER_PENALTY             = TraitInfo("Stutter Penalty", "57df5a8d-d805-48fc-b11b-25e15637de4e")

    # Ball Control
    FIRST_TOUCH                 = TraitInfo("First Touch", "d68b244c-6945-4115-96e8-fe9148bfd7b3")
    PRESS_PROVEN                = TraitInfo("Press Proven", "b40ccc84-6ab6-40de-a3cb-8934996a479e")

    # Physical
    QUICK_STEP                  = TraitInfo("Quick Step", "94be3e18-d04c-44c4-aea1-4857bba57a1b")
    BRUISER                     = TraitInfo("Bruiser", "797cfc8a-fc34-4bbd-a8bc-dd613e705276")
