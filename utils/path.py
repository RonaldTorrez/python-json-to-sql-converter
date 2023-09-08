import os
import shutil

from dotenv import load_dotenv

load_dotenv()


def base_dir() -> str:
	current_directory = os.path.dirname(__file__)
	return os.path.abspath(os.path.join(current_directory, ".."))


def file_path(file: str, directory: str) -> str:
	return directory + "/" + file


def generate_dirs():
	create_dir(result_dir())
	create_dir(json_dir())
	create_dir(sql_dir())


def create_dir(directory):
	if not is_validate_path(directory):
		os.makedirs(directory)


def is_validate_path(directory) -> bool:
	return os.path.exists(directory)


def result_dir() -> str:
	return base_dir() + "/" + os.getenv("RESULT_DIR")


def json_dir() -> str:
	return base_dir() + "/" + os.getenv("RESULT_JSON_DIR")


def sql_dir() -> str:
	return base_dir() + "/" + os.getenv("RESULT_SQL_DIR")


def data_dir() -> str:
	return base_dir() + "/" + os.getenv("DATA_DIR")


def clean_dir(directory: str):
	try:
		if is_validate_path(directory):
			shutil.rmtree(directory)
			create_dir(directory)
	except Exception as e:
		print(f"Error to clean {directory}: {e}")
