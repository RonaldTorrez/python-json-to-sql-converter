from data.loaddata import (
	load_country_data, load_country_official_lang_data, load_languages_data, load_regiones_data,
	load_subregiones_data
)
from utils.datetime import get_timestamp_tz
from utils.other import filter_data
from utils.savedata import save_csv, save_json, save_sql


def generate_files():
	save_name = "countries"
	data = []

	for country in load_country_data():
		obj = country.copy()
		obj.pop("timezones")
		obj.pop("translations")
		obj.pop("states")
		obj.pop("region")
		obj.pop("subregion")

		# ===============================
		# OFFICIAL LANGUAGE RELATION
		# ===============================

		obj["language_id"] = ""

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
				obj["language_id"] = lang[0]["id"]

		# ===============================
		# REGION RELATION
		# ===============================

		obj["region_id"] = ""

		if country["region"]:
			region = filter_data(
				load_regiones_data(),
				"name",
				country["region"]
			)

			if region:
				obj["region_id"] = region[0]["id"]

		# ===============================
		# SUBREGION RELATION
		# ===============================

		obj["subregion_id"] = ""

		if country["subregion"]:
			subregion = filter_data(
				load_subregiones_data(),
				"name",
				country["subregion"]
			)

			if subregion:
				obj["subregion_id"] = subregion[0]["id"]

		obj["created_at"] = get_timestamp_tz()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)
	print("\n")


if __name__ == "__main__":
	generate_files()
