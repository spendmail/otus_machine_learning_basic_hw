class AppException(Exception):
    pass


class LowFuelError(AppException):
    pass


class NotEnoughFuel(AppException):
    pass


class CargoOverload(AppException):
    pass
