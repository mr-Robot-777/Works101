
import json

with open('task1.json') as f:
  data = json.load(f)

img_keys = []

def find_img_keys(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if 'img' in key:
                num = int(key.split('_')[-1])
                img_keys.append(("img", num))
            find_img_keys(value)
    elif isinstance(obj, list):
        for item in obj:
            find_img_keys(item)

find_img_keys(data)

for key, num in img_keys:
    print(f"Key: {key}, Number: {num}")