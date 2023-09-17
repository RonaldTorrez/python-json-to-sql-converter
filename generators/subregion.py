from data.loaddata import (
	load_country_data, load_regiones_data,
	load_subregiones_data
)
from utils.datetime import get_timestamp_tz
from utils.other import filter_data
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "subregiones"
	data = []
	subregion_data = []

	for country in load_country_data():
		region = filter_data(
			load_regiones_data(),
			"name",
			country["region"]
		)

		subregion = filter_data(
			load_subregiones_data(),
			"name",
			country["subregion"]
		)

		for subreg in subregion:
			obj = subreg.copy()
			obj["region_id"] = region[0]["id"]
			obj["created_at"] = get_timestamp_tz()

			subregion_data.append(obj)

	data = [name for index, name in enumerate(subregion_data) if name not in subregion_data[:index]]

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)
	print("\n")


if __name__ == "__main__":
	generate_files()
