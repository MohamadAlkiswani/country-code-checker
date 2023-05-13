from countryCodeChecker.listOfCountries import CountryList

"""
example of how to run the code
"""

if __name__ == '__main__':
    countryList = CountryList()  # initializing the object

    us = countryList.get_country_of_code("us")
    #usa = countryList.get_code_of_country("Germany")
    #usaa = countryList.get_code_of_country("undas",True,3)
    print(us.get_name())

    exit()
