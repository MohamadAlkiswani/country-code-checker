class Country:
    """
    Countries describe a class which assign a country code to each country
    """
    name: str
    code2: str
    code3: str

    def __init__(self, name, code2, code3):
        self.name = name
        self.code2 = code2
        self.code3 = code3

    def get_code(self, length=2):
        """
        getter method
        :param length:2 or 3 representing the length of the code
        :return: returns the object's code
        """
        code = self.code2

        if length == 3:
            code = self.code3

        return code

    def get_name(self):
        """
        getter method
        :return: name of an object representing a country
        """
        return self.name
