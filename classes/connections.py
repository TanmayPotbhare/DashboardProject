class FellowshipHost:
    hostserver = '43.240.64.151'
    localserver = '127.0.0.1'
    host_fellowship = hostserver


class AadiswayamHost:
    hostserver = '43.240.64.78'
    localserver = '127.0.0.1'
    host_aadiswayam = hostserver


class ConnectParam:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        cnx = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        return cnx.cursor()


# class ConnectParam:
#     def __init__(self):
#         self.host_fellowship = FellowshipHost.host_fellowship
#         self.host_aadiswayam = AadiswayamHost.host_aadiswayam
#         self.projects = {
#             'fellowship': {'host': self.host_fellowship, 'user': 'root', 'password': 'A9CALcsd7lc%7ac', 'database': 'ICSApplication'},
#             'aadiswayam': {'host': self.host_aadiswayam, 'user': 'root', 'password': 'A>(I?mx|pt220uzE', 'database': 'aasiswayam_portaldb'},
#             # Define configurations for other projects
#         }
