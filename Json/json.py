import json


def read_json_file(file_path, key):
    with open(file_path, 'r') as f:
        data = json.load(f)
        if key in data:
            print(data[key])
        else:
            print(f"Ключ '{key}' не найден в файле")


# пример использования
file_path = 'example.json'  # путь к файлу
key = 'name'  # ключ, который нужно найти

read_json_file(file_path, key)

#
# В этом скрипте мы используем модуль json для чтения JSON файла. Функция read_json_file принимает два параметра: путь к файлу (file_path) и ключ, который нужно найти (key). Внутри функции мы открываем файл в режиме чтения ('r') и загружаем данные из файла с помощью метода json.load(). Затем мы проверяем, существует ли ключ в данных с помощью оператора in. Если ключ найден, мы выводим его значение на экран с помощью print(). Если ключ не найден, мы выводим сообщение об ошибке. Вы можете заменить example.json на путь к вашему JSON файлу и name на ключ, который вы хотите найти. Пример JSON файла (example.json):
#
# {
#     "name": "John",
#     "age": 30,
#     " occupation": "Developer"
# }
#
# Если вы запустите скрипт с параметрами file_path = 'example.json' и key = 'name', он выведет на экран значение John. Если у вас есть вложенный JSON объект, вы можете использовать точечную нотацию для доступа к вложенным ключам. Например, если у вас есть JSON файл со следующим содержимым:
#
# {
#     "user": {
#         "name": "John",
#         "age": 30
#     }
# }
#
# Вы можете использовать ключ user.name для доступа к значению John.
