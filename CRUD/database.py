from configparser import ConfigParser
import mysql.connector as mysql


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            return cls._instance
        cls._instance = super(Database, cls).__new__(cls)
        config = ConfigParser()
        config.read("Config/Config.ini")

        params = {
            "host": config.get("DB", "host"),
            "user": config.get("DB", "user"),
            "database": config.get("DB", "database"),
            "password": config.get("DB", "password")
        }
        cls._instance.connection = mysql.connect(**params)
        return cls._instance

    def get_connection(self):
        return self._instance.connection
