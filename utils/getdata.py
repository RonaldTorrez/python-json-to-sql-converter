import json

from utils.path import file_path


def get_json_data(name: str, directory: str) -> object:
    file = file_path(name, directory) + ".json"

    with open(file, "r", encoding="utf-8") as json_file:
        data: object = json.load(json_file)

    return data
