from data.loaddata import load_country_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_json, save_sql


def generate_files():
	save_name = "country_translates"
	data = []
	count = 0

	for country in load_country_data():
		if "es" in country["translations"]:
			count = count + 1
			obj = {
				"id": count,
				"lang": "es",
				"name": country["translations"]["es"],
				"country_id": country["id"],
				"created_at": get_timestamp_tz()
			}

			data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
