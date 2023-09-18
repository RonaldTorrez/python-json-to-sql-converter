from data.loaddata import load_country_data, load_languages_data
from utils.datetime import get_timestamp_tz
from utils.other import filter_data
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "country_translates"
	data = []
	count = 0

	for country in load_country_data():
		objs = country["translations"].copy()
		objs["ko"] = objs["kr"]
		objs.pop("kr")
		objs["zh"] = objs["cn"]
		objs.pop("cn")

		for key in objs:
			if "pt-BR" != key:
				count = count + 1
				lang = filter_data(
					load_languages_data(),
					"iso2",
					key
				)

				if lang:
					obj = {
						"id": count,
						"name": objs[key],
						"translate_language_id": lang[0]["id"],
						"translate_country_id": "",
						"country_id": country["id"],
						"created_at": get_timestamp_tz()
					}

					data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)


if __name__ == "__main__":
	generate_files()
