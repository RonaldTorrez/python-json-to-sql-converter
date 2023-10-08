from utils.print import print_error


def filter_data(data, attr: str, value) -> list:
	try:
		filtered_data = [obj for obj in data if obj.get(attr) == value]
		return filtered_data

	except Exception as e:
		print_error(f"Error to filer {attr}={value}", e)


def text_to_array(text: str, separator: str = ",", trim: bool = True) -> list:
	try:
		elements = text.split(separator)
		if trim:
			elements = [element.strip() for element in elements]

		return elements

	except Exception as e:
		print_error(f"Error to convert to Array = {text}", e)


def unique_key(json_data: [object]):
	keys = []

	for data in json_data:
		keys.extend(data.keys())

	keys = list(set(keys))

	return keys


def sort_obj(json_data: [object], order_by: str, asc: bool = True):
	return sorted(
		json_data,
		key=lambda x: getattr(x, order_by),
		reverse=not asc
	)
