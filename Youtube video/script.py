# Импортируем необходимые библиотеки
from pytube import YouTube
import os

# URL видео, которое мы хотим скачать
url = input("Введите ссылку: ")

# Путь к директории, в которую мы хотим сохранить видео
save_path = "./video"

# Создаем объект YouTube с помощью URL видео
yt = YouTube(url)

# Получаем поток с наивысшим разрешением
stream = yt.streams.get_highest_resolution()

# Скачиваем видео в указанную директорию
stream.download(output_path=save_path)
