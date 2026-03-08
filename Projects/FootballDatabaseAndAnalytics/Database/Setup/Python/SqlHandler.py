import os

from dotenv import load_dotenv
import mysql.connector

# Load environment variables
load_dotenv()

class SqlHandler:
    """
    Class to handle connection with MySQL databases
    Get configuration values from environment variables.
    """

    def __init__(self, database: str ="career_mode_legacy_db") -> None:
        """
        :param database: The name of the database to connect to.
        """
        # Read them
        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        # Connect to server (without DB first if creating)
        self.connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=database
        )

        self.cursor = self.connection.cursor()

    def get_result(self, table: str) -> None:
        """
        Function to get data from MySQL table
        Created for testing purposes
        :param table: The name of the table to get data from
        :param print_info: Optional string to print
        :return:
        """
        self.cursor.execute(f"SELECT * FROM {table};")

        columns = [col[0] for col in self.cursor.description]
        rows = self.cursor.fetchall()

        print(f"---{table}---")
        print(columns)
        for row in rows:
            print(row)
        print()

    def save_table_changes(self) -> None:
        """
        Function to save data changes to MySQL table
        :return:
        """
        self.connection.commit()
