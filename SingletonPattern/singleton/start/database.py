class Database:

    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def __str__(self):
        return f"{self.__name__}"
