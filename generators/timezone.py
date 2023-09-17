from data.loaddata import load_country_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "timezones"
	data = []

	for country in load_country_data():
		for entry in country["timezones"]:
			obj = {
				"name": entry["tzName"],
				"zone_name": entry["zoneName"],
				"tz": entry["gmtOffsetName"],
				"abbreviation": entry["abbreviation"],
				"country_id": country["id"],
				"created_at": get_timestamp_tz()
			}

			data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)
	print("\n")


if __name__ == "__main__":
	generate_files()
