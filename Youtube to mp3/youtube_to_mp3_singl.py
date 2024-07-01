import pytube
from moviepy.editor import AudioFileClip
import os

# ---1--- Функция которая копирует видео и конвертирует его в MP3

def youtube_to_mp3(url):
    # Создание объекта YouTube видео
    youtube = pytube.YouTube(url)

    # Выбираем первое видео с наивысшим разрешением
    video = youtube.streams.first()

    # Загружаем видео
    video.download()

    # Конвертируем видео в mp3
    audio = AudioFileClip(video.default_filename)
    audio.write_audiofile(video.default_filename[:-4] + ".mp3")

    # Удаляем исходный видеофайл
    os.remove(video.default_filename)

    # Вызываем функцию
# youtube_to_mp3("https://www.youtube.com/watch?v=98BpJ6JsQkU")

youtube_to_mp3(input("Введите ссылку:"))