import pytube
from moviepy.editor import AudioFileClip
import os


# ---2--- Функция которая копирует ссылки из файла а потом проходится по ним циклом

def process_line(line):
    # Создание объекта YouTube видео
    youtube = pytube.YouTube(line)

    # Выбираем первое видео с наивысшим разрешением
    video = youtube.streams.first()

    # Загружаем видео
    video.download()

    # Конвертируем видео в mp3
    audio = AudioFileClip(video.default_filename)
    audio.write_audiofile(video.default_filename[:-4] + ".mp3")

    # Удаляем исходный видеофайл
    os.remove(video.default_filename)


with open('1.txt', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        process_line(line.strip())
        if i == len(lines) - 1:
            print("Строки закончились.")
