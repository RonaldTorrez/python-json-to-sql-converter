import os

from dotenv import load_dotenv

from utils.getdata import get_json_data
from utils.path import data_dir

load_dotenv()


def load_country_data():
    return get_json_data(os.getenv(
        "COUNTRY_DATA_JSON"),
        data_dir()
    )
