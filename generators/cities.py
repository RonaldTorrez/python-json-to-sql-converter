from data.loaddata import load_country_data
from utils.datetime import get_timestamp
from utils.other import normalize_geodata
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "cities"
	data = []

	for country in load_country_data():
		for state in country["states"]:
			for entry in state["cities"]:
				obj = entry.copy()

				if obj["latitude"] == "0.00000000" and obj["longitude"] == "0.00000000":
					obj["latitude"] = normalize_geodata(obj["latitude"])
					obj["longitude"] = normalize_geodata(obj["longitude"])

				obj["country_id"] = country["id"]
				obj["state_id"] = state["id"]
				obj["created_at"] = get_timestamp()

				data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)


if __name__ == "__main__":
	generate_files()
