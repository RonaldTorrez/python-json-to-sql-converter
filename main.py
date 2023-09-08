from generators import cities, country, country_translate, state, timezone
from utils.path import clean_dir, generate_dirs, json_dir, sql_dir


def main():
	# ===============================
	# CREATE AND CLEAN RESULT FOLDER
	# ===============================

	generate_dirs()
	clean_dir(json_dir())
	clean_dir(sql_dir())

	print("cleaned")

	# ===============================
	# CREATE AND CLEAN RESULT FOLDER
	# ===============================

	country.generate_files()
	country_translate.generate_files()
	timezone.generate_files()
	state.generate_files()
	cities.generate_files()


if __name__ == "__main__":
	main()
