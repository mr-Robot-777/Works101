import json

def search(text, search_pattern, prev_datapoint_path=''):
    output = []
    current_datapoint = text
    current_datapoint_path = prev_datapoint_path
    if type(current_datapoint) is dict:
        for dkey in current_datapoint:
            if search_pattern in str(dkey):
                c = current_datapoint_path
                c += dkey +' '
                output.append(c)
            c = current_datapoint_path
            c += dkey +' '
            for i in search(current_datapoint[dkey], search_pattern, c):
                output.append(i)
    elif type(current_datapoint) is list:
        for i in range(0, len(current_datapoint)):
            if search_pattern in str(i):
                c = current_datapoint_path
                c +=  str(i) +' '
                output.append(i)
            c = current_datapoint_path
            c += str(i) +' '
            for i in search(current_datapoint[i], search_pattern, c):
                output.append(i)
    elif search_pattern in str(current_datapoint):
        c = current_datapoint_path
        output.append(c)
    output = filter(None, output)
    return list(output)


if __name__ == "__main__":
    with open('task1.json', 'r', encoding='utf-8') as f:
        text = json.load(f)

    zzz = 'img'
    # zzz = input("Введите значение поиска: ")

tt = search(text, zzz).pop(-1)

print(tt)


