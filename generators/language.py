from data.loaddata import load_languages_data, load_macrolanguages_data
from utils.datetime import get_timestamp_tz
from utils.savedata import save_json, save_sql
from utils.other import filter_data


def generate_files():
	save_name = "languages"
	data = []

	for language in load_languages_data():
		obj = language.copy()

		obj["macrolanguage_id"] = ""
		macro_lang = filter_data(
			load_macrolanguages_data(),
			"lang_id",
			language["iso3"]
		)

		if macro_lang:
			obj["macrolanguage_id"] = filter_data(
				load_languages_data(),
				"iso3",
				macro_lang[0]["macro_id"]
			)[0]["id"]

		obj["created_at"] = get_timestamp_tz()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)


if __name__ == "__main__":
	generate_files()
