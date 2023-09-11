import json

from utils.path import file_path
from utils.print import print_error


def get_json_data(name: str, directory: str) -> object:
	try:
		file = file_path(name, directory) + ".json"

		with open(file, "r", encoding="utf-8") as json_file:
			data: object = json.load(json_file)
			
		return data

	except Exception as e:
		print_error(f"Error to load {name}.json: ", e)
