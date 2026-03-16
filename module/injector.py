import json

from module.path import color # Импортирует путь к файлу цветов

def read_json_object(path): # Читает JSON файл и возвращает его содержимое | @pwaexho
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def injector_color(): # Читает цвет из JSON и возвращает его код | @pwaexho
    result = read_json_object(color)
    color_code = result["#DA70D6"]
    return color_code