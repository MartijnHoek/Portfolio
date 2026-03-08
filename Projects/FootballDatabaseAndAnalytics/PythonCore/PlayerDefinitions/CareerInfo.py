from dataclasses import dataclass

from CountryDefinitions.Countries import Countries
from CountryDefinitions.GeographicObjects import Country


@dataclass
class ClubObject:
    """ Dataclass to store the information about a club """
    name:       str             # Name of the club
    country:    Country         # Country that the club is based in
    uuid:       str             # Unique Identifier

@dataclass
class FifaVersionObject:
    """ Dataclass to store the information about the game version """
    name: str
    uuid: str

class Clubs:
    """ Class used to define all the clubs used in a career mode """
    BARCELONA           = ClubObject(name="FC Barcelona", country=Countries.SPAIN, uuid="663a75dd-35c9-4942-a871-f1759a4fe87c")
    PARIS_FC            = ClubObject(name="Paris FC", country=Countries.FRANCE, uuid="8bbe9b92-de9b-43a0-b92b-669e9f238365")
    SPARTA_ROTTERDAM    = ClubObject(name="Sparta Rotterdam", country=Countries.NETHERLANDS, uuid="4eaf6807-903e-4c4c-8640-06f1e6b3a4cd")
    TORINO              = ClubObject(name="Torino FC", country=Countries.ITALY, uuid="33777401-92b6-4e04-9449-88f208b0e67c")
    LIVERPOOL           = ClubObject(name="Liverpool FC", country=Countries.ENGLAND, uuid="16111855-1788-44e4-8982-ef1804661734")
    KFC_UERDINGEN       = ClubObject(name="KFC Uerdingen", country=Countries.GERMANY, uuid="0bcaf5e9-fb5d-49d7-8ae0-c500873b8f4d")
    FEYENOORD           = ClubObject(name="Feyenoord", country=Countries.NETHERLANDS, uuid="4c6d48b9-e8ee-4218-9d5e-0bd905cf5ab7")
    ACCRITON_STANLEY    = ClubObject(name="Accriton Stanley", country=Countries.ENGLAND, uuid="c6c317e6-4ce8-4bdd-83b3-cac59171d284")
    STOKE_CITY          = ClubObject(name="Stoke City FC", country=Countries.ENGLAND, uuid="2507f925-ae19-4be6-98c2-9bce7931d3d7")
    DORTMUND            = ClubObject(name="Borussia Dortmund", country=Countries.GERMANY, uuid="f686d90d-a228-4fd3-acab-077398d7b35d")
    BAYER_LEVERKUSSEN   = ClubObject(name="Bayer Leverkussen", country=Countries.GERMANY, uuid="fc3354a0-49f3-4bab-82c2-a60ca5288337")
    JUVENTUS            = ClubObject(name="Juventus", country=Countries.ITALY, uuid="071cd8b5-3cd1-422c-8f5f-37f3e406f25f")


class FifaVersion:
    """ Class used to define all the FIFA/EA FC versions """
    FIFA12 = FifaVersionObject("FIFA 12", "044dc8c5-e17c-4d56-9fd3-75cc325ad72d")
    FIFA13 = FifaVersionObject("FIFA 13", "39b38248-db41-44cf-86a4-648d6d2f2839")
    FIFA14 = FifaVersionObject("FIFA 14", "3457f88d-0d1b-4652-aad2-17173cd41620")
    FIFA15 = FifaVersionObject("FIFA 15", "a2952be7-7856-4f5f-b636-f610bbd1e833")
    FIFA16 = FifaVersionObject("FIFA 16", "29595de9-bf6d-408b-98c9-2099c7762959")
    FIFA17 = FifaVersionObject("FIFA 17", "ab21cd8e-c733-42da-a98e-a080e9b32fc1")
    FIFA18 = FifaVersionObject("FIFA 18", "5efeb950-92bc-4e8d-8695-7e1f07949087")
    FIFA19 = FifaVersionObject("FIFA 19", "5238928b-1766-47b7-ae8b-7775abf6d8b2")
    FIFA20 = FifaVersionObject("FIFA 20", "52b4d2b5-97ad-4e89-a8eb-efa5146b5719")
    FIFA21 = FifaVersionObject("FIFA 21", "72f6587f-6d22-49f5-bcdb-63c5851e667b")
    FIFA22 = FifaVersionObject("FIFA 22", "d5c5c88d-27bb-4d66-86fa-b49f6e676326")
    FIFA23 = FifaVersionObject("FIFA 23", "4cc69be4-041d-40b3-8025-9567e7adcb2b")
    FC24   = FifaVersionObject("FC 24", "08859ec1-dae0-440d-817f-b7f076b08788")

@dataclass
class CareerObject:
    """ Definition of hte CareerObject dataset"""
    fifa_version:           FifaVersionObject   # Object of the game version that the Career mode took place
    career_mode_year:       int                 # The year that the Career Mode was (needed to calculate the age)
    club:                   ClubObject          # The club that the Career Mode took place at
    uuid:                   str                 # Unique Identifier

class CareerMode:
    """ Class used to define all the different career modes CareerObjects """
    FIFA_12_JUVENTUS            = CareerObject(FifaVersion.FIFA12, 2013, Clubs.JUVENTUS, "b83af1e0-ecc5-4cec-b58c-4eaf4dee41bf")
    FIFA_13_JUVENTUS            = CareerObject(FifaVersion.FIFA13, 2020, Clubs.JUVENTUS, "4fc3f7b6-1119-43ce-8ce5-3e645b2428d8")
    FIFA_14_JUVENTUS            = CareerObject(FifaVersion.FIFA14, 2023, Clubs.JUVENTUS, "adf6a541-de62-48c4-a3c2-624f6a924c3d")
    FIFA_15_BARCELONA_YSL       = CareerObject(FifaVersion.FIFA15, 2027, Clubs.BARCELONA, "50c2167a-7a3c-4ff7-9b32-978ccca76a78")
    FIFA_15_BARCELONA           = CareerObject(FifaVersion.FIFA15, 2017, Clubs.BARCELONA, "2a486eba-0389-4ac4-bd60-8905449680cc")
    FIFA_15_BAYER_LEVERKUSSEN   = CareerObject(FifaVersion.FIFA15, 2019, Clubs.BAYER_LEVERKUSSEN, "75ff172f-cb41-467c-9ba4-304998c81e96")
    FIFA_16_DORTMUND            = CareerObject(FifaVersion.FIFA16, 2022, Clubs.DORTMUND, "b3c44941-7873-49e5-84ac-868c27421a34")
    FIFA_16_FEYENOORD           = CareerObject(FifaVersion.FIFA16, 2021, Clubs.FEYENOORD, "c76d8f60-fe13-496f-aa6a-5dceda9aeeb7")
    FIFA_17_STOKE_CITY          = CareerObject(FifaVersion.FIFA17, 2024, Clubs.STOKE_CITY, "11f7aed4-1e51-464c-9e0f-4394a9091b62")
    FIFA_18_ACCRITON_STANLEY    = CareerObject(FifaVersion.FIFA18, 2028, Clubs.ACCRITON_STANLEY, "ac567797-9c22-4b1c-a8df-33c68c16040d")
    FIFA_19_FEYENOORD           = CareerObject(FifaVersion.FIFA19, 2025, Clubs.FEYENOORD, "d8b047f5-6fe0-49b0-9fcf-e6bddb734ab8")
    FIFA_20_KFC_UERDINGEN       = CareerObject(FifaVersion.FIFA20, 2027, Clubs.KFC_UERDINGEN, "db0cdf2e-49a0-46b7-8de7-eeaa9cdfe587")
    FIFA_21_SPARTA_ROTTERDAM    = CareerObject(FifaVersion.FIFA21, 2029, Clubs.SPARTA_ROTTERDAM, "b19a7a94-ef8b-4599-abc7-a6a5134788ff")
    FIFA_22_LIVERPOOL           = CareerObject(FifaVersion.FIFA22, 2027, Clubs.LIVERPOOL, "0fb5cee8-de4e-4b18-98b5-0d4421ed3f52")
    FIFA_23_BARCELONA           = CareerObject(FifaVersion.FIFA23, 2025, Clubs.BARCELONA, "9675e504-78ec-47b6-a4d6-da1606074f1d")
    FIFA_23_TORINO              = CareerObject(FifaVersion.FIFA23, 2034, Clubs.TORINO, "2ffa7d7d-a9d6-4486-8b44-b307a34194a7")
    FC_24_PARIS_FC              = CareerObject(FifaVersion.FC24,   2028, Clubs.PARIS_FC, "16580c18-76ad-49c0-873d-f4df551e54ba")