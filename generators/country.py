from data.loaddata import (
	load_country_data, load_country_official_lang_data, load_languages_data, load_regiones_data,
	load_subregiones_data
)
from utils.datetime import get_timestamp
from utils.other import filter_data, normalize_geodata
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

		if obj["latitude"] == "0.00000000" and obj["longitude"] == "0.00000000":
			obj["latitude"] = normalize_geodata(obj["latitude"])
			obj["longitude"] = normalize_geodata(obj["longitude"])

		# ===============================
		# OFFICIAL LANGUAGE RELATION
		# ===============================

		obj["official_language_id"] = None

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
				obj["official_language_id"] = lang[0]["id"]

		# ===============================
		# REGION RELATION
		# ===============================

		obj["region_id"] = None

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

		obj["subregion_id"] = None

		if country["subregion"]:
			subregion = filter_data(
				load_subregiones_data(),
				"name",
				country["subregion"]
			)

			if subregion:
				obj["subregion_id"] = subregion[0]["id"]

		obj["created_at"] = get_timestamp()

		data.append(obj)

	save_json(save_name, data)
	save_sql(save_name)
	save_csv(save_name)


if __name__ == "__main__":
	generate_files()
