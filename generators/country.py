from data.loaddata import load_country_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_json, save_sql


def generate_files():
	save_name = "countries"
	data = []

	for country in load_country_data():
		obj = country.copy()
		obj.pop("timezones")
		obj.pop("translations")
		obj.pop("states")

		obj["created_at"] = get_timestamp_tz()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
