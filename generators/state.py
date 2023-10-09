from data.loaddata import load_country_data
from utils.datetime import get_timestamp
from utils.other import normalize_geodata
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "states"
	data = []

	for country in load_country_data():
		for entry in country["states"]:
			obj = entry.copy()
			obj.pop("cities")

			if obj["latitude"] == "0.00000000" and obj["longitude"] == "0.00000000":
				obj["latitude"] = normalize_geodata(obj["latitude"])
				obj["longitude"] = normalize_geodata(obj["longitude"])

			obj["country_id"] = country["id"]
			obj["created_at"] = get_timestamp()

			data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)


if __name__ == "__main__":
	generate_files()
