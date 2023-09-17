import json

from utils.path import file_path, json_dir
from utils.print import print_error


def get_json_data(filename: str, directory: str = json_dir()) -> [object]:
	try:
		file = file_path(filename, directory) + ".json"

		with open(file, "r", encoding="utf-8") as json_file:
			data: object = json.load(json_file)

		return data

	except Exception as e:
		print_error(f"Error to load {filename}.json: ", e)
