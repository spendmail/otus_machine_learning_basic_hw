from src.errors import NotImplementedMethodError, NotImplementedInterfaceError
from src.services import FileSystem, S3, Storage


class Media:
    """Basic class for all media types.

    Possesses common properties.

    Takes respective services that implements Storage interface
    in order to work with different storages and file systems.
    """

    def __init__(self, file_path: str, storage: Storage = FileSystem()):
        if not isinstance(storage, Storage):
            raise NotImplementedInterfaceError('storage must be an instance of Storage interface')

        self.storage = storage
        self.file_path = file_path
        self.name, self.size, self.c_date, self.m_date, self.owner = self.load(file_path)

    def load(self, file_path: str):
        return self.storage.read(file_path)

    def save(self, file_path: str):
        self.storage.save(self, file_path if file_path is not None else self.file_path)

    def delete(self):
        self.storage.delete(self)


class Video(Media):
    """Implementation for working with video types.

    Reliable for encoding video into different formats.
    """
    MIME_TYPE_MP4 = 'video/mp4'
    MIME_TYPE_AVI = 'video/avi'

    def __init__(self, file_path: str, storage: Storage = FileSystem()):
        super().__init__(file_path, storage=storage)

    @classmethod
    def load_video(cls, file_path):
        return Video(file_path)

    @classmethod
    def load_video_from_s3(cls, file_path):
        return Video(file_path, storage=S3())

    def encode(self, fmt: str):
        raise NotImplementedMethodError('method encode is not implemented yet')


class Audio(Media):
    """Implementation for working with audio types.

    Reliable for converting audio into different formats.
    """

    MIME_TYPE_MP3 = 'audio/mpeg'
    MIME_TYPE_FLAC = 'audio/flac'

    def __init__(self, file_path: str, storage: Storage = FileSystem()):
        super().__init__(file_path, storage=storage)

    @classmethod
    def load_audio(cls, file_path):
        return Audio(file_path)

    @classmethod
    def load_audio_from_s3(cls, file_path):
        return Audio(file_path, storage=S3())

    def convert(self, fmt: str):
        raise NotImplementedMethodError('method convert is not implemented yet')


class Image(Media):
    """Implementation for working with images.

    Reliable for cropping images.
    """

    def __init__(self, file_path: str, storage: Storage = FileSystem()):
        super().__init__(file_path, storage=storage)

    @classmethod
    def load_image(cls, file_path):
        return Image(file_path)

    @classmethod
    def load_image_from_s3(cls, file_path):
        return Image(file_path, storage=S3())

    def crop(self, x, y, width, height):
        raise NotImplementedMethodError('method crop is not implemented yet')
