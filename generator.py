import json
import os

# =============================
# FOLDERS
# =============================

result_path = './result'
result_json_path = result_path + '/json'
result_sql_path = result_path + '/sql'

def mkdir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

mkdir(result_json_path)
mkdir(result_sql_path)


# =============================
# FUNCTIONS
# =============================

def generateSQL (table):
    # Load the JSON file
    with open("./result/json/" + table + ".json", 'r') as json_file:
            data = json.load(json_file)

    fields = set()

    for obj in data:
        fields.update(obj.keys())

    fields = list(fields)
    fields_with_quotes = ['"{}"'.format(field) for field in fields]

    sql_insert = f"INSERT INTO {table} ({', '.join(fields_with_quotes)}) VALUES "
    sql_values = []

    for obj in data:
        values = [str(obj.get(field, '')) for field in fields]
        values = [value.replace("'", "''") if "'" in value else value for value in values]
        values = [', '.join(["'" + str(value) + "'" for value in values])]

        statement = f"({', '.join(values)});"

        sql_values.append(statement)

    with open("./result/sql/" + table + ".sql", 'w', encoding='utf-8') as sql_file:
        sql_file.write(sql_insert + '\n'.join(sql_values))

    print(table.upper() + " sql generated.")



def generateJSON(name, data):
    with open("./result/json/"+ name +".json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(name.upper() + " json generated.")




# =============================
# GENERATION JSONs STRUCTURE
# =============================

with open("data.json", "r", encoding="utf-8") as json_file:
    original_data = json.load(json_file)

countries_data = []
timezones_data = []
translations_data = []
states_data = []
cities_data = []

for entry in original_data:
    country_entry = entry.copy()
    country_entry.pop("timezones")
    country_entry.pop("translations")
    country_entry.pop("states")
    countries_data.append(country_entry)

    if "timezones" in entry:
        for timezone_entry in entry["timezones"]:
            timezone_entry_with_country = timezone_entry.copy()
            timezone_entry_with_country["country_id"] = entry["id"]
            timezones_data.append(timezone_entry_with_country)

    if "states" in entry:
        for state_entry in entry["states"]:
            state_entry_with_country = state_entry.copy()
            state_entry_with_country.pop("cities")
            state_entry_with_country["country_id"] = entry["id"]
            states_data.append(state_entry_with_country)

            if "cities" in state_entry:
                for city_entry in state_entry["cities"]:
                    city_entry_with_state = city_entry.copy()
                    city_entry_with_state["state_id"] = state_entry["id"]
                    city_entry_with_state["country_id"] = entry["id"]
                    cities_data.append(city_entry_with_state)

    if "es" in entry["translations"]:
        translation_entry = {
            "lang": "es",
            "name": entry["translations"]["es"],
            "country_id": entry["id"]
        }
        translations_data.append(translation_entry)



# =============================
# RUN FUNCTIONS
# =============================

generateJSON("countries", countries_data)
generateSQL("countries")

generateJSON("timezones", timezones_data)
generateSQL("timezones")

generateJSON("translations", translations_data)
generateSQL("translations")

generateJSON("states", states_data)
generateSQL("states")

generateJSON("cities", cities_data)
generateSQL("cities")