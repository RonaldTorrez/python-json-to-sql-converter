from data.loaddata import load_country_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_json, save_sql


def generate_files():
	save_name = "timezones"
	data = []
	count = 0

	for country in load_country_data():
		for tz in country["timezones"]:
			count = count + 1
			obj = {
				"id": count,
				"name": tz["tzName"],
				"zone_name": tz["zoneName"],
				"tz": tz["gmtOffsetName"],
				"abbreviation": tz["abbreviation"],
				"country_id": country["id"],
				"created_at": get_timestamp_tz()
			}

			data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
