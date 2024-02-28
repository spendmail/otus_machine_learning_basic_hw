from hw_03.entities import Image, Audio, Video
from hw_03.errors import NotImplementedInterfaceError

if __name__ == '__main__':

    try:
        video = Video.load_video('/path/to/video.mp4')
        video.encode(Video.MIME_TYPE_AVI)
        video.save('/path/to/video.avi')
    except NotImplementedInterfaceError as e:
        print(e)
    except Exception as e:
        print(e)

    try:
        audio = Audio.load_audio('/path/to/audio.mp3')
        audio.convert(Audio.MIME_TYPE_FLAC)
        audio.save('/path/to/audio.flac')
    except NotImplementedInterfaceError as e:
        print(e)
    except Exception as e:
        print(e)

    try:
        image = Image.load_image_from_s3('s3://path/to/image.jpg')
        image.crop((0, 100, 200, 300))
        image.save('/path/to/image.jpg')
    except NotImplementedInterfaceError as e:
        print(e)
    except Exception as e:
        print(e)
