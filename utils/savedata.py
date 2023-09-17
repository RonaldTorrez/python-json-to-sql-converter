import csv
import json

from utils.getdata import get_json_data
from utils.path import csv_dir, file_path, json_dir, sql_dir
from utils.print import print_error, print_saved


def save_json(name: str, data, directory: str = json_dir()):
	try:
		file = name + ".json"
		file_dir = file_path(file, directory)

		with open(file_dir, "w", encoding="utf-8") as json_file:
			json.dump(data, json_file, indent=4, ensure_ascii=False)

		print_saved(file)

	except Exception as error:
		print_error(f"Error to save {name}.json", error)


def save_sql(json_filename: str, table_name: str = "", directory: str = sql_dir()):
	try:
		table_name = json_filename if not table_name else table_name
		file = table_name + ".sql"
		file_dir = file_path(file, directory)

		data = generate_sql_structure(
			get_json_data(json_filename),
			table_name
		)

		with open(file_dir, 'w', encoding='utf-8') as sql_file:
			sql_file.write(data)

		print_saved(file)

	except Exception as error:
		print_error(f"Error to save {table_name}.sql", error)


def generate_sql_structure(json_data: [object], table_name: str):
	fields = set()

	for obj in json_data:
		fields.update(obj.keys())

	fields = list(fields)
	fields_with_quotes = ['"{}"'.format(field) for field in fields]

	sql_insert = f"INSERT INTO {table_name} ({', '.join(fields_with_quotes)}) VALUES "
	sql_values = []

	for obj in json_data:
		values = [str(obj.get(field, '')) for field in fields]
		values = [value.replace("'", "''") if "'" in value else value for value in values]
		values = [', '.join([None if value is None else "'" + str(value) + "'" for value in values])]

		values = f"({', '.join(values)})"

		sql_values.append(values)

	return sql_insert + ',\n'.join(sql_values)


def save_csv(json_filename: str, directory: str = csv_dir()):
	file = json_filename + ".csv"
	file_dir = file_path(file, directory)
	json_data = get_json_data(json_filename)

	headers = unique_key(json_data)

	with open(file_dir, encoding='utf-8', mode="w", newline="") as csv_file:
		writer = csv.writer(csv_file, delimiter="\t")
		writer.writerow(headers)

		for obj in json_data:
			values = []
			for head in headers:
				if head in obj:
					values.append(obj[head])

			if values:
				writer.writerow(values)

	print_saved(file)


def unique_key(json_data: [object]):
	keys = []

	for data in json_data:
		keys.extend(data.keys())

	keys = list(set(keys))

	return keys

# print(
# 	unique_key(
# 		file_path("countries.json", json_dir())
# 	)
# )
