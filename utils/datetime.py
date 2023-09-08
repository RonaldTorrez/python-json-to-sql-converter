from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_timestamp_tz():
    return get_timestamp() + " +00:00"
