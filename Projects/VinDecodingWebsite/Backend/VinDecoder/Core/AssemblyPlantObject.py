class EmptyCountry:
    """
    Class created to mimic the Country object of pycountry.db.Country but instead of string as values return None for each property
    """
    def __init__(self):
        self.alpha_2=            None
        self.alpha_3=            None
        self.flag=               None
        self.name=               None
        self.numeric=            None
        self.official_name=      None

class AssemblyPlantObject:
    def __init__(self, name=None, city=None, region=None, country=EmptyCountry(), uuid=None):
        self.name =     name
        self.city =     city
        self.region =   region
        self.country =  country     # pycountry.db.Country Object
        self.uuid =     uuid
