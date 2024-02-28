from src.errors import NotImplementedInterfaceError


class Storage:
    """Basic storage interface.

    Defines a number of methods to work with filesystems and other storages.
    """

    def read(self, file_path: str):
        raise NotImplementedInterfaceError('method read is not implemented yet')

    def save(self, media, file_path: str):
        raise NotImplementedInterfaceError('method save is not implemented yet')

    def delete(self, media):
        raise NotImplementedInterfaceError('method delete is not implemented yet')


class FileSystem(Storage):
    """Implementation to work with a filesystem."""

    pass


class S3(Storage):
    """Implementation to work with S3 based file storages."""

    pass
