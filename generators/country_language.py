from data.loaddata import (
	load_country_data, load_country_official_lang_data, load_country_other_lang_data, load_languages_data
)
from utils.datetime import get_timestamp_tz
from utils.other import filter_data, text_to_array
from utils.savedata import save_json, save_sql


def generate_files():
	save_name = "country_language"
	data = []
	count = 0

	for country in load_country_data():
		official_lang = filter_data(
			load_country_official_lang_data(),
			"country_iso2",
			country["iso2"]
		)

		country_other_lang = filter_data(
			load_country_other_lang_data(),
			"country_iso2",
			country["iso2"]
		)

		if country_other_lang:
			for lang_relation in text_to_array(country_other_lang[0]["languages_iso2"]):
				lang = filter_data(
					load_languages_data(),
					"iso2",
					lang_relation
				)

				if lang:
					count = count + 1
					is_official_lang = official_lang[0]["language_iso2"] if official_lang else None
					is_official_lang = 1 if is_official_lang == lang[0]["iso2"] else 0

					obj = {
						"id": count,
						"country_id": country["id"],
						"language_id": lang[0]["id"],
						"is_official": is_official_lang,

						"created_at": get_timestamp_tz()
					}

					data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
