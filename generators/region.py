from data.loaddata import load_regiones_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "regiones"
	data = []

	for region in load_regiones_data():
		obj = region.copy()
		obj["created_at"] = get_timestamp_tz()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)
	print("\n")


if __name__ == "__main__":
	generate_files()
