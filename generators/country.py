from data.loaddata import load_country_data, load_country_official_lang_data, load_languages_data
from utils.datetime import get_timestamp_tz
from utils.other import filter_data
from utils.savedata import save_json, save_sql


def generate_files():
	save_name = "countries"
	data = []

	for country in load_country_data():
		obj = country.copy()
		obj.pop("timezones")
		obj.pop("translations")
		obj.pop("states")
		obj["official_lang"] = ""

		official_lang = filter_data(
			load_country_official_lang_data(),
			"country_iso2",
			country["iso2"]
		)

		if official_lang:
			lang = filter_data(
				load_languages_data(),
				"iso2",
				official_lang[0]["language_iso2"]
			)
			if lang:
				obj["official_lang"] = lang[0]["id"]

		obj["created_at"] = get_timestamp_tz()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
