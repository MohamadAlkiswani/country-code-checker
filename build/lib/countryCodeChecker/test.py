"""
test script
"""

import json
#from countryCodeChecker.CountryCode import Country
import importlib_resources as ii
from countryCodeChecker.listOfCountries import CountryList

countryList = CountryList()

with ii.path("countryCodeChecker", "countries_with_codes.json") as data_path:
    with open(data_path, encoding="utf-8") as f:  # opening json file
        data = json.load(f)


def test():
    """
    a simple test method
    """
    for d in data:
        code2 = d["2letter"]
        out2 = countryList.get_country_of_code(code2)
        code3 = d["2letter"]
        out3 = countryList.get_country_of_code(code3)
        name = d["name"]
        outN = countryList.get_code_of_country(name)

        assert d["2letter"] in outN

        assert d["name"] in out2

        assert d["name"] in out3

    print("test was successful")
