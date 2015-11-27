class HttpException(Exception):
    """base exception for http request"""
    def __init__(self, message=None, details=None, status_code=None):
        self.message = self.__class__.__name__ if message is None else message
        super(Exception, self).__init__(self.message)
        self.details = details
        self.status_code = status_code

    def __unicode__(self):
        msg = self.__class__.__name__ + ": " + self.message
        if self.details:
            msg += ", " + self.details
        return msg

    def __str__(self):
        return self.__unicode__()


class NotFoundException(HttpException):
    """404"""
    def __init__(self, message=None, details=None, status_code=None):
        super(NotFoundException, self).__init__(message, details, status_code)


class InvalidResponse(HttpException):
    """response from server is not valid for this request."""
    def __init__(self, response):
        super(InvalidResponse, self).__init__()
        self.response = response
