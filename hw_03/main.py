from src.entities import Video, Audio, Image
from src.errors import NotImplementedInterfaceError

if __name__ == '__main__':

    # This example represents working with video files.
    source_path = '/path/to/video.mp4'
    result_path = '/path/to/video.avi'
    try:
        video = Video.load_video(source_path)
        video.encode(Video.MIME_TYPE_AVI)
        video.save(result_path)
    except NotImplementedInterfaceError as e:
        msg = f"""
(Class video is being launched in a demo mode cause a few methods are not implemented yet) 
Loading {source_path}... done!
Encoding... done!
Saving {result_path}... done!
        """
        print(msg)
    except Exception as e:
        print(e)

    # This example represents working with audio files.
    source_path = '/path/to/audio.mp3'
    result_path = '/path/to/audio.flac'
    try:
        audio = Audio.load_audio(source_path)
        audio.convert(Audio.MIME_TYPE_FLAC)
        audio.save(result_path)
    except NotImplementedInterfaceError as e:
        msg = f"""
(Class Audio is being launched in a demo mode cause a few methods are not implemented yet) 
Loading {source_path}... done!
Converting... done!
Saving {result_path}... done!
        """
        print(msg)
    except Exception as e:
        print(e)

    # This example represents working with images.
    source_path = 's3://path/to/image.jpg'
    try:
        image = Image.load_image_from_s3(source_path)
        image.crop((0, 100, 200, 300))
        image.save()
    except NotImplementedInterfaceError as e:
        msg = f"""
(Class Image is being launched in a demo mode cause a few methods are not implemented yet) 
Loading {source_path}... done!
Cropping... done!
Saving... done!
        """
        print(msg)
    except Exception as e:
        print(e)
