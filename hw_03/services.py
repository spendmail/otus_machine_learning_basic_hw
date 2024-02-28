from hw_03.errors import NotImplementedInterfaceError


class Storage:
    def read(self, file_path: str):
        raise NotImplementedInterfaceError('method read is not implemented yet')

    def save(self, media, file_path: str):
        raise NotImplementedInterfaceError('method save is not implemented yet')

    def delete(self, media):
        raise NotImplementedInterfaceError('method delete is not implemented yet')


class FileSystem(Storage):
    pass


class S3(Storage):
    pass
