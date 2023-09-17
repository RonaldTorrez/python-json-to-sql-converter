from utils.getdata import get_json_data
from utils.path import data_dir


def load_country_data():
	return get_json_data(
		"countries_data",
		data_dir()
	)


def load_country_official_lang_data():
	return get_json_data(
		"countries_official_language",
		data_dir()
	)


def load_country_other_lang_data():
	return get_json_data(
		"countries_other_languages",
		data_dir()
	)


def load_languages_data():
	return get_json_data(
		"languages",
		data_dir()
	)


def load_macrolanguages_data():
	return get_json_data(
		"macrolanguages",
		data_dir()
	)


def load_regiones_data():
	return get_json_data(
		"regiones",
		data_dir()
	)


def load_subregiones_data():
	return get_json_data(
		"subregiones",
		data_dir()
	)
