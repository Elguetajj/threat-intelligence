class AppInfoException(Exception):
    ...


class AppInfoNotFoundError(AppInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "App Info Not Found"


class AppInfoInfoAlreadyExistError(AppInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "App Info Already Exists"