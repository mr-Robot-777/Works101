import json

with open('task1.json', 'r', encoding='utf-8') as f:
    text = json.load(f)


def PrintKey(string):
    return string[:3]


def PrintValue(string):
    return string[4:]


if 'section' in text:
    if 'notes' in text['section'][1]:
        if 'news_date' in text['section'][1]['notes'][1]:
            for key, value in text['section'][1]['notes'][1].items():
                print(key, value)
                for ss in key:
                    if ss.endswith('date'):
                        print(f'Найдено {format(ss)}')
                        print(f'Разбитие на ключи и значения "{PrintKey(ss)}" : "{PrintValue(ss)}"')
