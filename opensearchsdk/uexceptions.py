# -*- encoding: utf-8 -*-
class CommandError(Exception):
    pass


class OpenSearchException(Exception):
    def __str__(self):
        return "Error"


class ConnectionRefused(Exception):
    """
    Connection refused: the server refused the connection.
    """

    def __init__(self, response=None):
        self.response = response

    def __str__(self):
        return "ConnectionRefused: %s" % repr(self.response)


class NoJsonFound(Exception):
    """
    no json object was found
    """

    def __init__(self, response=None):
        self.response = response

    def __str__(self):
        return "NoJsonFound: %s" % repr(self.response)


class BadParameters(Exception):
    """
    no value return since bad parameters
    """

    def __init__(self, response=None):
        self.response = response

    def __str__(self):
        return "BadParameters: %s" % repr(self.response)


