from generators import (
	cities, country, country_language, country_translate, language, region, state, subregion, timezone
)
from utils.path import generate_dirs


def main():
	# ===============================
	# CREATE AND CLEAN RESULT FOLDER
	# ===============================

	generate_dirs()

	print("cleaned")

	# ===============================
	# CREATE AND CLEAN RESULT FOLDER
	# ===============================

	country.generate_files()
	country_translate.generate_files()
	timezone.generate_files()
	state.generate_files()
	cities.generate_files()
	language.generate_files()
	country_language.generate_files()
	region.generate_files()
	subregion.generate_files()


if __name__ == "__main__":
	main()
