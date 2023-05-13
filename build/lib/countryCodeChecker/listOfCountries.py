from countryCodeChecker.CountryCode import Country
import json
import unidecode
import importlib_resources as ii


class CountryList:
    """
    class that has a list of countries as objects
    and methods that give the regional code of a country and vice versa
    """

    def __init__(self):
        with ii.path("countryCodeChecker", "countries_with_codes.json") as data_path:
            with open(data_path, encoding="utf-8") as f:  # opening json file
                data = json.load(f)

        self.countries = []  # initiating the list with all countries objects

        for d in data:
            country = Country(
                name=d["name"],
                code2=d["2letter"],
                code3=d["3letter"]
            )
            self.countries.append(country)  # appending country to the list

    def __get_country_c(self, code):
        """
        a helper method that returns an object country from a code
        :param code: the country's code
        return: Country object
        """

        for i in range(len(self.countries)):
            if len(code) == 2:
                if self.countries[i].get_code(2).lower() in code.lower():
                    return self.countries[i]
            elif len(code) == 3:
                if self.countries[i].get_code(3).lower() in code.lower():
                    return self.countries[i]

        return None  # returns None if country not found

    def __get_country(self, name):
        """
        a helper method that returns an object country from a name
        :param name: the country's name
        :return: Country object or a list of similar countries
        """
        listofpredicitions = []
        for i in range(len(self.countries)):
            if len(name) != len(self.countries[i].get_name().lower()):
                if unidecode.unidecode(name.lower()) in unidecode.unidecode(self.countries[i].get_name().lower()):
                    listofpredicitions.append(self.countries[i].get_name())
                continue
            if unidecode.unidecode(name.lower()) in unidecode.unidecode(self.countries[i].get_name().lower()):
                return self.countries[i]

        return listofpredicitions

    def get_code_of_country(self, name, prnt=False, length=2):
        """
        return the object of a country given its name
        :param name: the name of the country
        :param prnt: True prints the code, False returns it as a string
        :param length: 2 OR 3, represent the length of the regional code
        :return: an object of a country according to the given name
        """
        country = self.__get_country(name=name)
        if type(country) is list:  # check if similar countries were found
            if not country:  # Country not found
                print("country does not exist")
                return None
            print("do you mean one of these countries?")  # printing the similar countries
            print(*country, sep='\n')
            return False

        if length == 3:
            if prnt:
                print(country.get_code(3))
                return True
            return country
        if prnt:
            print(country.get_code(2))
            return True
        return country

    def get_country_of_code(self, code, name=False):
        """
        returns the object country given its code
        :param code: the given code of a country that needs to be found
        :param name: decides whether to print the country's name or not
        :return: an object of a country representing according to the given code
        """
        if len(code) > 3 or len(code) < 2:  # checking the code's length
            print("country does not exist")
            return

        country = self.__get_country_c(code)  # searching for the country is done here

        if country is None:
            print("country does not exist")
            return

        if name:  # check if the country's name is needed to be printed
            print(country.get_name())
            return True

        return country
