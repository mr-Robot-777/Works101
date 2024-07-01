import schedule
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import shutil

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def upload_dir(dir_path=''):
    try:
        drive = GoogleDrive(gauth)

        for file_name in os.listdir(dir_path):
            my_file = drive.CreateFile({'title': f'{file_name}'})
            my_file.SetContentFile(os.path.join(dir_path, file_name))
            my_file.Upload()

            print(f'Файл {file_name} успешно загружен!')

        return mov()

    except Exception as _ex:
        return 'Возникли некоторые проблемы, проверьте свой код, пожалуйста!'


def mov():
    file_source = '111/34/' # Директория откуда будут перемещены файлы
    file_destination = '111/upload/' # Директория куда будут перемещены файлы
    get_files = os.listdir(file_source)

    for g in get_files:
        shutil.move(file_source + g, file_destination)

    print(f'Файлы перемещены в директорию {file_destination}')


def main():
    print(upload_dir(dir_path='111/34')) # Директория откуда будут забираться файлы для загрузки


schedule.every(5).seconds.do(main)                   #
# schedule.every().minutes.do(main)                  #
# schedule.every().hour.do(main)                     #
# schedule.every().day.at("10:30").do(main)          # Выбрать нужное время для повторения
# schedule.every().to(10).minutes.do(main)           #
# schedule.every().monday.do(main)                   #
# schedule.every().wednesday.at("13:15").do(main)    #
# schedule.every().minute.at(":17").do(main)         #

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main()
