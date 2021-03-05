# START PROBLEM SET 09 
print('Problem set 09 \n')

# SETUP
import csv

class Country():
    """
    Representation of a country

    Attributes:
        code (str): the code of the country
        name (str): the name of the country
        population (int): the population of the country
        meat_consumption_per_capita (dict): the meat consumption per capita of the country
        meat_co2_emission_per_capita (float): the co2 emission caused by consumption of meat per capita of the country
        meat_co2_emission_total (float): the total co2 emission caused by consumption of meat of the country
    """
    # Problem 1
    def __init__(self, code, name, population): # TODO complete the parameter list
        """
        The constructor of the < Country > class. Here you will need to create
        the attributes ("instance variables") that were described in the < Country >
        docstring. Note that some of the attributes are defined by parameters passed
        to this constructor method, but others are not.

        Parameters:
            code (str): The code of the country
            name (str): The name of the country
            population (int): The population of the country

        Returns:
            None
        """
        self.code = code
        self.name = name
        self.population = population
        self.meat_consumption_per_capita = {}
        self.meat_co2_emission_per_capita = 0.0
        self.meat_co2_emission_total = 0.0

    # Problem 2
    def __str__(self):
        """
        This is the string method for the < Country > class. Whenever an instance of
        < Country > is passed to the str() or print() functions, the return string
        from this method will be returned.

        Parameters:

            None
        Returns:
            str: A string that describes this instance of < Country >
        """
        return f"{self.name} ({self.code}) emitted {self.meat_co2_emission_per_capita} kg co2 caused by meat consumption per capita and {self.meat_co2_emission_total} kg in total"

    # Problem 3
    def add_meat_consumption(self, meat_type, consumption):
        """
        This method will modify <meat_consumption_per_capita> by adding a new key:value pair 
        where <meat_type> is the key and <consumption> is the value.

        Parameters:
            meat_type (str): Type of the meat.
            consumption (float): Consumption(kg) of the meat 

        Returns:
            None
        """
        self.meat_consumption_per_capita[meat_type] = float(consumption)

    # Problem 4
    def calculate_emission_per_capita(self, meat_emission):
        """
        This method will modify <meat_co2_emission_per_capita> by increasing 
        its value with co2 emission of different types of meat.

        Parameters:
            meat_emission (dict): Key is type of the meat and value is co2 emission (kg) of corresponding meat.
        
        Returns:
            None
        """
        meat_co2_per_capita = 0.0
        for key, value in self.meat_consumption_per_capita.items():
            meat_co2_per_capita += meat_emission[key] * float(value)
        self.meat_co2_emission_per_capita = meat_co2_per_capita

    # Problem 5
    def calculate_total_emission(self):
        """
        This method will modify <meat_co2_emission_total> by multiply <population> 
        with <meat_co2_emission_per_capita>.

        Parameters:
            None

        Returns:
            None
        """
        self.meat_co2_emission_total = (self.meat_co2_emission_per_capita * self.population)

# Problem 6
def write_to_file(filepath, data):
    """
    This function takes any < data >, converts it into a string via the str()
    function (if possible), and then writes it to a file located at < filepath >. Note
    that this function is a general writing function. It should not use the .csv
    module, but rather the python write() function. This is because we want this
    function to write ANYTHING we give it as the < data > parameter (in the
    case of this assignement, you will actually use it to write string representations
    of the class instances you create).
    
    NOTE: It is important that you convert < data > to a str BEFORE you write it!
    The object being passed into this function as < data > could already be a
    string, and if so, passing it through the str() function won't do anything. But
    any other object will need to be changed into a string object.
    
    Parameters:
        filepath (str): the filepath that points to the file that will be written.
        data (obj): any object capable of being converted into a string.
    
    Returns:
        None, but a file is produced.
    """

    with open(filepath, 'w', encoding= 'utf-8') as file_object:
        file_object.write(str(data))


# We provide the read_csv function for you
def read_csv(filepath):
    """Returns a list of dictionaries where each dictionary is formed from the data.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of dictionaries where each dictionary is formed from the data
    """
    
    with open(filepath, mode='r', newline='', encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data

def main():
    """Program entry point. Handles program workflow.

    Parameters:
        None

    Returns:
       usa (str)
       usa_meat_consumption_per_capita (dict)
       usa2 (str)
       max_country (obj)
       min_country (obj)
    """

    meat_emission = {
        'BEEF': 27.0,
        'PIG': 12.1,
        'SHEEP': 39.2,
        'POULTRY': 6.9,
    }

    ### Problem 7.1
    country_population = read_csv('./country_population.csv')
    country_meat_consumption = read_csv('./country_meat_consumption.csv')
    #print(country_meat_consumption)

    ### Problem 7.2
    countries = {}
    for i in country_population:
        converted_to_class = Country(i['Code'], i['Name'], float(i['Population(m)']) * (1000000))
        countries[i['Code']] = converted_to_class
    
    usa = countries['USA'].__str__()
    #print(usa)

    ### Problem 7.3
    
    
    for consumption in country_meat_consumption:
        meat_t = consumption['TYPE']
        consump = float(consumption['CONSUMPTION'])
        code = consumption['CODE']
        country_instance = countries[code]
        country_instance.add_meat_consumption(meat_t, consump)
    
    usa_meat_consumption_per_capita = countries['USA'].meat_consumption_per_capita
    #print(usa_meat_consumption_per_capita)

    ### Problem 7.4
    for country in countries:
        Country.calculate_emission_per_capita(countries[country], meat_emission)
        Country.calculate_total_emission(countries[country])
    
    usa2 = str(countries['USA'])
    #print(usa2)
    ### Problem 7.5
    max_co2 = 0.0
    min_co2 = 1000000000000000000.0
    for country in countries.values():
        if country.meat_co2_emission_per_capita > max_co2:
            max_co2 = country.meat_co2_emission_per_capita
            max_country = country
        if country.meat_co2_emission_per_capita < min_co2:
            min_co2 = country.meat_co2_emission_per_capita
            min_country = country

    write_to_file('max_country.txt', max_country.__str__())
    write_to_file('min_country.txt', min_country.__str__())
    # Don't forget to return variables
    # If you want to test your code before you finish all the PS, 
    # you can assign None to those return variables
    return usa, usa_meat_consumption_per_capita, usa2, max_country, min_country
#Do not delete the lines below.
if __name__ == '__main__':
    main()
