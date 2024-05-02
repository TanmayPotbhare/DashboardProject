import mysql.connector


class FellowshipHost:
    def __init__(self):
        self.hostserver = '43.240.64.151'
        self.localserver = '127.0.0.1'


class AdiswayamHost:
    def __init__(self):
        self.central = '192.168.10.50'
        self.hostserver = '43.240.64.78'
        self.localserver = '127.0.0.1'


class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
