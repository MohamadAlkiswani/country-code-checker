"""
test script
"""
import unittest
import json
import importlib_resources as ii
from countryCodeChecker.listOfCountries import CountryList


class TestCountries(unittest.TestCase):

    def test(self):
        """
        a simple test method
        """
        countryList = CountryList()

        with ii.path("countryCodeChecker", "countries_with_codes.json") as data_path:
            with open(data_path, encoding="utf-8") as f:  # opening json file
                data = json.load(f)

        for d in data:
            code2 = d["2letter"]
            out2 = countryList.get_country_of_code(code2).get_name()
            code3 = d["2letter"]
            out3 = countryList.get_country_of_code(code3).get_name()
            name = d["name"]
            outN = countryList.get_code_of_country(name).get_code()

            self.assertIn(d["2letter"], outN)

            self.assertIn(d["name"], out2)

            self.assertIn(d["name"], out3)

        print("test was successful")


if __name__ == '__main__':
    unittest.main()
