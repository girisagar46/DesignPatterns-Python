class _Database:  # Make the class private

    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def __str__(self):
        return f"{self.__name__}"


_instance = None  # create a private _instance variable


# Create a function with same name of our private class except the underscore
def Database(host, port, user, passwd):
    global _instance  # to make sure we are manipulating the global variable
    if _instance is None:
        _instance = _Database(host, port, user, passwd)
    return _instance
