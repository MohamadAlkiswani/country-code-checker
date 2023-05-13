from listOfCountries import CountryList


if __name__ == '__main__':
    countryList = CountryList()  # initializing the object

    countryList.get_country_of_code("us", True)
    countryList.get_code_of_country("Curacao", True)


    exit()
