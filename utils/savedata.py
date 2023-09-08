import json

from utils.path import file_path, json_dir, sql_dir
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


def save_sql(json_name: str, table_name: str = '', directory: str = sql_dir()):
	try:
		table_name = json_name if not table_name else table_name
		file = table_name + ".sql"
		file_dir = file_path(file, directory)

		data = generate_sql_structure(
			file_path(f"{json_name}.json", json_dir()),
			table_name
		)

		with open(file_dir, 'w', encoding='utf-8') as sql_file:
			sql_file.write(data)

		print_saved(file)

	except Exception as error:
		print_error(f"Error to save {table_name}.sql", error)


def generate_sql_structure(json_data: str, table_name: str):
	with open(json_data, 'r') as json_file:
		data = json.load(json_file)

	fields = set()

	for obj in data:
		fields.update(obj.keys())

	fields = list(fields)
	fields_with_quotes = ['"{}"'.format(field) for field in fields]

	sql_insert = f"INSERT INTO {table_name} ({', '.join(fields_with_quotes)}) VALUES "
	sql_values = []

	for obj in data:
		values = [str(obj.get(field, '')) for field in fields]
		values = [value.replace("'", "''") if "'" in value else value for value in values]
		values = [', '.join([None if value is None else "'" + str(value) + "'" for value in values])]

		values = f"({', '.join(values)})"

		sql_values.append(values)

	return sql_insert + ',\n'.join(sql_values)
