""""""
""" 01 Воспроизведение мультимедиа

Создайте два класса:
Класс 1

AudioFileMixin — требует наличие атрибута audio_tracks (список треков).


Метод play_audio() выводит:
Воспроизведение аудио для <НазваниеКласса>:
	<название трека>
	<название трека>

Класс 2

VideoFileMixin — требует наличие атрибута video_files (список видео).


Метод play_video() выводит:
Воспроизведение видео для <НазваниеКласса>:
	<название видео>
	<название видео>

Если нужное поле отсутствует — выбрасывайте AttributeError.
"""

"""Create a class AudioFileMixin """
class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audios"):
            raise AttributeError
        print(f"Playing audio for {self.__class__.__name__}")
        for i in self.audios:
            print(i)



class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "videos"):
            raise AttributeError
        print(f"Playing video for {self.__class__.__name__}")
        for i in self.videos:
            print(i)


# Проверим в следующем задании!

""" 02 Устройства

Создайте два класса:
MediaPlayer — поддерживает только аудио. Принимает список треков.
Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.

!!! Не забудьте проверить наличие атрибутов в КАЖДОМ объекте
"""

# from homework_01 import AudioFileMixin, VideoFileMixin


# Класс MediaPlayer — поддерживает только аудио
class MediaPlayer(AudioFileMixin):
    def __init__(self, audios):
        self.audios = audios


# Класс Laptop — поддерживает и аудио, и видео
class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audios, videos):
        self.audios = audios
        self.videos = videos



# Примеры использования
player = MediaPlayer(["Song 1", "Song 2"])
laptop = Laptop(["Song A", "Song B"], ["Video X", "Video Y"])


player.play_audio()

# try:
#     player.play_video()
# except AttributeError as e:
#     print(f'{e.__class__.__name__}: {e}')

print()
laptop.play_audio()
laptop.play_video()

# Воспроизведение аудио для MediaPlayer:
# 	Песня 1
# 	Песня 2
# AttributeError: 'MediaPlayer' object has no attribute 'play_video'
#
# Воспроизведение аудио для Laptop:
# 	Песня A
# 	Песня B
# Воспроизведение видео для Laptop:
# 	Видео X
# 	Видео Y