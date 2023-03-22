# Country Code Check

a package to return the country of a given code or vice versa

### Installing

1. install it from pip with the name "countryCodeChecker"
```sh
	pip install countryCodeChecker
   ```
2. import the package in your project 
 ```sh
   from countryCodeChecker import listOfCountries
   ```
3. create an object of the countries list
ex:
 ```sh
   countries = listOfCountries.CountryList()
   ```

## Usage
1. prints code of country
```sh
	countries.get_code_of_country("Australie", True)   
   ```
2. prints country of a given code
```sh
	countries.get_country_of_code("AU", True)   
   ```
3. return an object country of a given code
```sh
	usa = countries.get_country_of_code("US")
	print(usa.get_name())   
   ```


## Contact

Oezdemir Akdemir - Oezdemir.Akdemir@adastragrp.com

Johannes Mellenthin - Johannes.Mellenthin@adastragrp.com

Mohamad Alkiswani - mohamad.alkiswani@adastragrp.com

Project Link: [pythonlab-country-code-check](https://tfs.adastragrp.com/tfs/DefaultCollection/_git/pythonlab-country-code-check)


## Author
* **Mohamad Alkiswani**