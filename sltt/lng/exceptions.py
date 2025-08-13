class LngException(Exception):
    def __init__(self, message):
        self.message = message


class LngValidationError(LngException):
    pass


class LngLoadingError(LngException):
    pass
