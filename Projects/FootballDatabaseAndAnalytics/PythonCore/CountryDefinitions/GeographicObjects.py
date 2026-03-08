class Region(object):
    """
    Object that stores information about a region, used to define the regio a player comes from.
    This can be used to separate countries for qualifiers for example
    """
    def __init__(self, name, uuid):
        """
        :param name: The name of the region (string)
        :param uuid: An unique identifier for the region (string)
        """
        self.name = name            # String
        self.uuid = uuid            # String

    def __repr__(self):
        """ Defined represent to make object easier to read
        :return: Print region info as Region(name=Africa, uuid=...)
        """
        return f"Region(name={self.name!r}, uuid={self.uuid!r})"

class Country(object):
    """
    Object that defines a country, used to define that country that a player comes from
    """
    def __init__(self, name, region, uuid):
        self.name = name            # String
        self.region = region        # Region Object
        self.uuid = uuid            # String

    def __repr__(self):
        """ Defined represent to make object easier to read
        :return: Print country info as Country(name=Netherlands, region=Europe, uuid=....)
        """
        return f"Country(name={self.name!r}, region={self.region!r}, uuid={self.uuid!r})"