class MediaError(Exception):
    pass


class NotImplementedClassError(MediaError):
    pass


class NotImplementedMethodError(MediaError):
    pass


class NotImplementedInterfaceError(MediaError):
    pass
