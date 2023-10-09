from data.loaddata import load_languages_data, load_macrolanguages_data
from utils.datetime import get_timestamp
from utils.other import filter_data
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "languages"
	data = []

	for language in load_languages_data():
		obj = language.copy()
		obj["microlanguage_id"] = None

		micro_lang = filter_data(
			load_macrolanguages_data(),
			"lang_id",
			language["iso3"]
		)

		if micro_lang:
			obj["microlanguage_id"] = filter_data(
				load_languages_data(),
				"iso3",
				micro_lang[0]["macro_id"]
			)[0]["id"]

		obj["created_at"] = get_timestamp()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)


if __name__ == "__main__":
	generate_files()
