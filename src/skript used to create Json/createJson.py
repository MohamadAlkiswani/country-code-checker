import json
import csv

"""
Creating a Json file with only countries names
and their codes in the following format:
[{
        "name": "Germany",
        "2letter": "DE",
        "3letter": "DEU"
    }]
"""

with open('countries_with_codes.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)
    data = []
    # Check file as empty
    if header != None:
        # Iterate over each row after the header in the csv
        for row in csv_reader:
            # append each row to the list
            data.append(row)

whole_dict = []

for index, name, code2, code3 in data:
    # a dictionary for each country
    dict_country = {"name": name, "2letter": code2, "3letter": code3}
    # the big dictionary with all the countries
    whole_dict.append(dict_country)

with open('countries_with_codes.json', 'w') as f:
    # saving the dictionary as a Json file
    json.dump(whole_dict, f, indent=4, ensure_ascii=False)
print(whole_dict)
