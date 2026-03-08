from pandas import pandas, Series
from scipy.stats import stats
from CareerLegacyDb.Setup.Python.SqlHandler import SqlHandler


class AnalyticsTooling:
    """
    Class to keep Notebooks simple and keep most of the import logic here
    """
    def __init__(self) -> None:
        # Connect to the SQL database
        self.sql_handler = SqlHandler()
        self.dataframes = {}

        self.get_dataframes()

    def get_dataframes(self) -> None:
        """
        Get the data from SQL and convert them to a DataFrame, store the dataframes in self.dataframes dict
        :return: None
        """
        query = "SELECT * FROM person_info;"
        self.dataframes["df_person_info"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM player_info;"
        self.dataframes["df_player_info"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM player_ratings;"
        self.dataframes["df_player_ratings"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM career_modes;"
        self.dataframes["df_career_modes"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM countries;"
        self.dataframes["df_countries"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM regions;"
        self.dataframes["df_regions"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM game_versions;"
        self.dataframes["df_game_versions"] = pandas.read_sql(query, con=self.sql_handler.connection)

        query = "SELECT * FROM clubs;"
        self.dataframes["df_clubs"] = pandas.read_sql(query, con=self.sql_handler.connection)

    @staticmethod
    def get_correlation_value(value1: tuple[str, Series], value2: tuple[str, Series]) -> None:
        """
        Function to get and print the correlation value between two series.
        :param value1: tuple (Name of series 1, series 1)
        :param value2: tuple (Name of series 2, series 2)
        """
        correlation_value = value1[1].corr(value2[1])
        print(f"[i] {value1[0]} and {value2[0].lower()} correlation value is: {correlation_value}")

        if 0.7 <= correlation_value <= 1:
            print(f"[i] This is a strong positive relation.")
        elif 0.3 <= correlation_value < 0.7:
            print(f"[i] This is a moderate positive relation.")
        elif 0 <= correlation_value < 0.3:
            print(f"[i] This is a weak positive relation.")
        else:
            print(f"[i] This is a negative relation.")

    @staticmethod
    def get_p_value(value1: tuple[str, Series], value2: tuple[str, Series], alpha: float = 0.05) -> None:
        """
        Function to get and print the statistical significance value between two series.
        :param value1: tuple (Name of series 1, series 1)
        :param value2: tuple (Name of series 2, series 2)
        :param alpha: significance level (default 0.05)
        """
        corr_height_weight, p_value_height_weight = stats.pearsonr(value1[1], value2[1])

        value1_str = value1[0].lower()
        value2_str = value2[0].lower()

        print(f"[i] The p-value is {p_value_height_weight}")
        if p_value_height_weight < alpha:
            print(f"[i] This means {value1_str} and {value2_str} are statistically significant.")
        else:
            print(f"[i] This means {value1_str} and {value2_str} are not statistically significant.")
