class MediaError(Exception):
    """Basic package exception"""

    pass


class NotImplementedClassError(MediaError):
    """Exception is thrown if a class is not implemented"""

    pass


class NotImplementedMethodError(MediaError):
    """Exception is thrown if a class method is not implemented"""

    pass


class NotImplementedInterfaceError(MediaError):
    """Exception is thrown if a class interface is not implemented"""

    pass
