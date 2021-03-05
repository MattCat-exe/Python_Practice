import csv
import json
import os
import requests


class Crew:
    """Representation of a Starship or Vehicle crew.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in key-value pairs.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to generate each instance variable and assign the value. The
        dictionary key (e.g., "pilot") will serve as the instance variable name to which the
        accompanying < Person > or < Droid > instance value will be assigned.

        Parameters:
            members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variables
        and converts person objects to dictionaries. Do not simply return self.__dict__. It can
        be intercepted and mutated, adding, modifying or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person object

        return crew


class Droid:
    """Representation of a mechanical beings that possessed artificial intelligence.

    Attributes:
        url (str): identifier/locator
        name (str): droid name
        model (str): droid model
        manufacturer (str): creator
        create_year (str): droid's year of manufacture (akin to birth_year)
        height (float): droid's height in meters
        mass (float): droid's mass in kilograms
        equipment (list): droid's equipment, if any
        instructions (list): language modules, flight plans, etc.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model, manufacturer, create_year, height, mass, equipment):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.create_year = create_year
        self.height = height
        self.mass = mass
        self.equipment = equipment
        self.instructions = []

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def store_instructions(self, instructions):
        """Provide droid with special instructions such as language modules, flight
        plans, etc.

        Parameters:
            instructions (dict): nested dictionary of key-value pairs of instructions

        Returns:
            None
        """

        self.instructions.append(instructions)

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal
        rather than a built-in dict() to avoid built-in lookup costs. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing
        instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'manufacturer': self.manufacturer,
            'create_year': self.create_year,
            'height': self.height,
            'mass': self.mass,
            'equipment': self.equipment,
            'instructions': self.instructions
       }


class Passengers:
    """Representation of a passengers carried on a Starship or Vehicle.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in list of < Person > and/or < Droid > objects. The instance name format
        is described in the < __init__() > method Docstring.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid >objects and calls the built-in function < setattr() > to generate the instance
        variable and assign the value. The name of each < Droid > or < Person > will serve as
        the instance variable name (format: lowercase with spaces replaced by underscores, e.g.,
        "Luke Skywalker" to "luke_skywalker") to which the accompanying < Person > or < Droid >
        instance value will be assigned.

        Parameters:
            passengers (list): list of < Person > objects

        Returns:
            None
        """

        for passenger in passengers:
            setattr(self, passenger.name.lower().replace(' ', '_'), passenger) # call built-in function

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = val.name # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variable
        values and converts passenger < Person > objects to dictionaries. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing instance
        attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """
        Passengers_list = []
        for val in self.__dict__.values():
            Passenger = val.jsonable() # person object
            Passengers_list.append(Passenger.jsonable())
        return Passengers_list


class Person:
    """Representation of a person.

    Attributes:
        url: identifer/locator
        name: person name
        birth_year: person's birth_year
        homeworld: person's home planet
        species (list): species of person

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, height, mass):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.mass = mass
        self.homeworld = None
        self.species = None

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """
        if self.homeworld:
            instance_homeworld = self.homeworld.jsonable()
        else:
            instance_homeworld = None
        if self.species:
            instance_species = self.species.jsonable()
        else:
            instance_species = None
        return {
            'url': self.url,
            'name': self.name,
            'birth_year': self.birth_year,
            'height': self.height,
            'mass': self.mass,
            'homeworld': instance_homeworld,
            'species': instance_species
        }


class Planet:
    """Representation of a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in days
        diameter_km (int): diameter of planet measured in kilometers
        gravity (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, region, sector, suns, moons, orbital_period_days,
                diameter_km, gravity, climate, terrain, population):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.region = region
        self.sector = sector
        self.suns = suns
        self.moons = moons
        self.orbital_period_days = orbital_period_days
        self.diameter_km = diameter_km
        self.gravity = gravity
        self.climate = climate
        self.terrain = terrain
        self.population = population


    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
                'url': self.url,
                'name': self.name,
                'region': self.region,
                'sector': self.sector,
                'suns': self.suns,
                'moons': self.moons,
                'orbital_period_days': self.orbital_period_days,
                'diameter_km': self.diameter_km,
                'gravity': self.gravity,
                'climate': self.climate,
                'terrain': self.terrain,
                'population': self.population
            }


class Species:
    """A unit of biodiversity.

    Attributes:
        url (str): identifier/locator
        name (str): common name
        classification (str): classifier (e.g., 'mammal', 'reptile')
        designation (str): designation (e.g., 'sentient')
        language (str): language commonly spoken by species

    Methods:
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name, classification, designation, language):
        """Initialize a Species instance."""

        self.url = url
        self.name = name
        self.classification = classification
        self.designation = designation
        self.language = language

    def __str__(self):
        """Human-readable string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        return {
                'url': self.url,
                'name': self.name,
                'classification': self.classification,
                'designation' : self.designation,
                'language' : self.language
            }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length (float): starship length
        max_atmosphering_speed (int): max sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew (int): crew size
        crew_members (Crew): Crew instance assigned to starship
        passengers (int): number of passengers starship rated to carry
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity (float): cargo metric tonnage starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished


    Methods:
        assign_crew: assign crew members to starship
        assign_passengers: assign passengers to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class, manufacturer, length,
                max_atmosphering_speed, hyperdrive_rating, MGLT, armament, crew,
                passengers, cargo_capacity, consumables):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.armament = armament
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.crew_members = None
        self.passengers_on_board = None

    def __str__(self):
        """String representation of the object."""

        return str(self.model)

    def add_passengers(self, passengers):
        """Add passengers to starship if passenger accommodations are available.

        Parameters:
            passengers (Passengers): Passengers object containing Person instances

        Returns:
            None
        """
        if self.passengers > 0:
            setattr(self, 'passengers_on_board', passengers)

    def assign_crew_members(self, crew):
        """Assign crew_members.

        Parameters:
            crew (Crew): Object comprising crew members (role, person)

        Returns:
            None
        """

        setattr(self, 'crew_members', crew)

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """
        if self.crew_members:
            starship_crew = self.crew_members.jsonable()
        else:
            starship_crew = None
        if self.passengers_on_board:
            starship_passengers = self.passengers_on_board.jsonable()
        else:
            starship_passengers = None
        return{
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew': self.crew,
            'crew_members': starship_crew,
            'passengers': self.passengers,
            'passengers_on_board': starship_passengers,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables
        }


def clean_data(data):
    """Convert < data > string values to provided types. < var_types > provides a mapping
    of an object's instance variables that can be converted from a string to a more
    appropriate type (e.g., 'float', 'int', 'list'). Each < var_type > key name
    corresponds to a type while each value is a tuple of instance variable names whose
    values can be converted.

    For each < data > key-value pair with a value that is not None, the function performs
    the following operations:
        1. Checks if value is a string (use isinstance(val, str))
        2. if the string value is "n/a", "none", or "unknown" the value is converted to None.
        3. Checks if < var_types > has key (e.g., if 'float' in var_types.keys()) and if
           < data > key can be found in the < var_type > key's tuple values. If the membership
           check returns True the corresponding value is converted to the type specified by the
           < var_type > key name (e.g. 'float').
        3. When splitting strings into lists the delimiter is assumed to be ', '.

    Parameters:
        data (dict): string values to convert

    Returns
        dict: updated key-value pairs
    """

    # key-value pairs that map a tuple of instance variable names to a given type (the key name)
    var_types = {
        'float': ('height', 'hyperdrive_rating', 'length', 'mass', 'orbital_period_days'),
        'int': ('cargo_capacity', 'crew', 'diameter_km', 'max_atmosphering_speed', 'moons', 'MGLT', 'passengers', 'population', 'suns'),
        'list': ('armament', 'climate', 'equipment', 'terrain')
    }

    cleaned = {}
    for key, val in data.items():
        if isinstance(val, str):
            if val in ('n/a', 'none', 'unknown', ''):
                val = None
                cleaned[key] = val
            elif key in var_types['float']:
                val = float(val)
                cleaned[key] = float(val)
            elif key in var_types['int']:
                val = int(val)
                cleaned[key] = int(val)
                continue
            elif key in var_types['list']:
                val = val.split(', ')
                cleaned[key] = val
                continue
            else:
                cleaned[key] = val

        else:
            cleaned[key] = val # non str key-value pairs
            continue
    return cleaned


def create_droid(data):
    """Creates a Droid instance from dictionary data, converting string values to the appropriate
    type whenever possible. Adding special instructions constitutes a seperate operation.

    Parameters:
        data (dict): source data

    Returns:
        Droid: new Droid instance
    """

    Droid_instance = Droid(data['url'], data['name'], data['model'], data['manufacturer'], data['create_year'], data['height'], data['mass'], data['equipment'])
    return Droid_instance

def create_person(data, planets=None):
    """Creates a Person instance from dictionary data, converting string values to the appropriate
    type whenever possible. Calls < get_swapi_resource() > to retrieve homeworld and species data.
    Calls < create_planet() > and < create_species() > to add homeworld and species objects to the
    person instance.

    Parameters:
        data (dict): source data
        planets (list): supplemental planetary data

    Returns:
        Person: new Person instance
    """

    # Instantiate person

    person_instance = Person(data['url'], data['name'], data['birth_year'], data['height'], data['mass'])

    # Get, combine, clean data, and instantiate Planet instance

    if data.get('homeworld'):
        homeworld_data = get_swapi_resource(data['homeworld'])
        if planets:
            planet_data = get_wookieepedia_planet(planets, homeworld_data['name'])
        if planet_data:
            homeworld_data.update(planet_data)
            clean_hw = clean_data(homeworld_data)
            homeworld_data.update(clean_hw)
        person_instance.homeworld = create_planet(homeworld_data)

    # Get, clean data, and instantiate a new Species instance

    if 'species' in data.keys():
        species_data = get_swapi_resource(data['species'][0])
        clean_sp = clean_data(species_data)
        species_data.update(clean_sp)
        person_instance.species = create_species(species_data)

    return person_instance


def create_planet(data):
    """Creates a Planet instance from dictionary data, converting string values to the
    appropriate type whenever possible.

    Parameters:
        data (dict): source data

    Returns:
        Planet: new Planet instance
    """

    Planet_instance = Planet(data['url'], data['name'], data['region'], data['sector'], data['suns'], data['moons'], data['orbital_period_days'], data['diameter_km'], data['gravity'], data['climate'], data['terrain'], data['population'])
    return Planet_instance


def create_species(data):
    """Returns a Species instance from provided dictionary data.

    Parameters:
        data (dict): source data

    Returns:
        Species: new Species instance
    """

    Species_instance = Species(data['url'], data['name'], data['classification'], data['designation'], data['language'])
    return Species_instance



def create_starship(data):
    """Creates a Starship instance from dictionary data, converting string values to the
    appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Parameters:
        data (dict): source data

    Returns:
        starship: a new Starship instance
    """

    starship_instance = Starship(data['url'], data['name'], data['model'], data['starship_class'], data['manufacturer'], data['length'], data['max_atmosphering_speed'], data['hyperdrive_rating'], data['MGLT'], data['armament'], data['crew'], data['passengers'], data['cargo_capacity'], data['consumables'])
    return starship_instance


def get_swapi_resource(url, params=None, timeout=10):
    """This function initiates an HTTP GET request to the SWAPI service in order to return a
    representation of a resource. <params> is not included in the request if no params is passed to this
    function during the function call. Once a response is received, it is converted to a python dict.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        data = requests.get(url, params).json() # pass search parameters as 2nd argument
    else:
        data = requests.get(url + '/').json()
    return data


def get_wookieepedia_planet(planets, name):
    """Returns planet data sourced from Wookieepedia, if any, per provided planet
    name.

    Parameters:
        planets (list): list of planet dictionarys
        name (str): name of planet to locate

    Returns:
        dict: planet dictionary
    """

    for planet in planets:
        if planet['name'] == name:
            return planet
        else:
            continue


def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, mode='r', newline='', encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for program."""

    endpoint = 'https://swapi.py4e.com/api'

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    abs_path = os.path.dirname(os.path.abspath(__file__))
    print(f"\n0.0: Absolute directory path = {abs_path}")

    # Example: absolute filepath (create)
    #filepath = os.path.join(abs_path, 'stu_swapi_species_wookiee.json')

    # Example: relative filepath
    #filepath = 'stu_swapi_species_wookiee.json'


    # CHALLENGE 02 SPECIES
    wookiee_data = get_swapi_resource("https://swapi.py4e.com/api/species/", params={'search':'wookiee'})['results'][0]
    Wookiee = create_species(wookiee_data)
    filepath_wookiee = 'stu_swapi_species_wookiee.json'
    write_json(filepath_wookiee, Wookiee.jsonable())

    # CHALLENGE 03 PLANET
    hoth_data = get_swapi_resource('https://swapi.py4e.com/api/planets/', params={'search':'hoth'})['results'][0]
    wookiee_planets = read_csv_into_dicts('./wookieepedia_planets.csv')
    hoth_data.update(wookiee_planets[5])
    hoth = create_planet(hoth_data)
    filepath_hoth = 'stu_swapi_planet_hoth.json'
    write_json(filepath_hoth, hoth.jsonable())

    # CHALLENGE 04 DROID
    r2_d2_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'r2-d2'})['results'][0]
    wookiee_droids = read_json('./wookieepedia_droids.json')
    r2_d2_data.update(wookiee_droids[-1])
    r2_d2 = create_droid(r2_d2_data)
    filepath_r2 = 'stu_swapi_droid_r2_d2.json'
    write_json(filepath_r2, r2_d2.jsonable())

    # CHALLENGE 05 PERSON

    leia_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Leia'})['results'][0]
    wookiee_people = read_json('./wookieepedia_people.json')
    leia_data.update(wookiee_people[4])
    leia = create_person(leia_data, wookiee_planets)
    filepath_leia = 'stu_swapi_person_leia.json'
    write_json(filepath_leia, leia.jsonable())


    # CHALLENGE 07 STARSHIP

    x_wing_data = get_swapi_resource('https://swapi.py4e.com/api/starships/', params={'search': 'T-70 X-wing'})['results'][0]
    wookiee_starships = read_csv_into_dicts('./wookieepedia_starships.csv')
    x_wing_data.update(wookiee_starships[1])
    x_wing = create_starship(x_wing_data)
    filepath_xwing = 'stu_swapi_starship_x_wing.json'
    write_json(filepath_xwing, x_wing.jsonable())


    # CHALLENGE 08 CLEAN_DATA()

    x_wing_clean = clean_data(x_wing_data)
    x_wing_data.update(x_wing_clean)
    x_wing = create_starship(x_wing_data)
    write_json(filepath_xwing, x_wing.jsonable())

    # CHALLENGE 09. MISSION TO JAKKU

    poe_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Poe Dameron'})['results'][0]
    poe_data.update(wookiee_people[6])
    poe_clean = clean_data(poe_data)
    poe_data.update(poe_clean)
    poe = create_person(poe_data, wookiee_planets)

    bb8_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'BB8'})['results'][0]
    bb8_data.update(wookiee_droids[0])
    bb8_clean = clean_data(bb8_data)
    bb8_data.update(bb8_clean)
    bb8 = create_droid(bb8_data)
    
    jakku_data = get_swapi_resource('https://swapi.py4e.com/api/planets/', params={'search': 'jakku'})['results'][0]
    jakku_data.update(wookiee_planets[7])
    jakku_clean = clean_data(jakku_data)
    jakku_data.update(jakku_clean)
    jakku = create_planet(jakku_data)
    
    flight_plan = {
        'flight_plan': {
            'destination': jakku.jsonable(),
            'hyperspace_route': "Burke's Trailing",
            'year': "34 ABY"
            }
    }

    bb8.store_instructions(flight_plan)

    lor_data = (wookiee_people[5])
    lor_clean = clean_data(lor_data)
    lor_data.update(lor_clean)
    lor = create_person(lor_data, wookiee_planets)

    lor_instructions = {
        'locate_person': lor.jsonable()
    }

    bb8.store_instructions(lor_instructions)
    jakku_crew = Crew({'pilot': poe, 'astro_mech_droid': bb8})
    x_wing.assign_crew_members(jakku_crew)
    filepath_jakku = 'stu_episode_vii_mission_jakku.json'
    write_json(filepath_jakku, x_wing.jsonable())


    # CHALLENGE 10 STAR MAP (ATTACK ON TUANUL)

    wookiee_star_map = read_json('./wookieepedia_star_map.json')
    clean_star = clean_data(wookiee_star_map)
    wookiee_star_map.update(clean_star)
    star_instruction = {
        'star_map': wookiee_star_map
    }

    bb8.store_instructions(star_instruction)

    filepath_star = 'stu_episode_vii_star_map.json'
    write_json(filepath_star, bb8.jsonable())


    # CHALLENGE 11 ESCAPE FROM JAKKU

    rey_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Rey'})['results'][0]
    rey_data.update(wookiee_people[7])
    clean_rey = clean_data(rey_data)
    rey_data.update(clean_rey)
    rey = create_person(rey_data, wookiee_planets)

    finn_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Finn'})['results'][0]
    finn_data.update(wookiee_people[1])
    clean_finn = clean_data(finn_data)
    finn_data.update(clean_finn)
    finn = create_person(finn_data, wookiee_planets)

    m_falcon_data = get_swapi_resource('https://swapi.py4e.com/api/starships/', params={'search': 'Millennium Falcon'})['results'][0]
    m_falcon_data.update(wookiee_starships[4])
    clean_falcon = clean_data(m_falcon_data)
    m_falcon_data.update(clean_falcon)
    m_falcon = create_starship(m_falcon_data)

    m_falcon_crew = Crew({'pilot': rey, 'gunner': finn})
    m_falcon.assign_crew_members(m_falcon_crew)
    m_falcon_passengers = Passengers([bb8])
    m_falcon.add_passengers(m_falcon_passengers)

    filepath_falcon = 'stu_episode_vii_escape-jakku.json'
    write_json(filepath_falcon, m_falcon.jsonable())



    # CHALLENGE 12 JOURNEY TO TAKODANA

    han_solo_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Han Solo'})['results'][0]
    han_solo_data.update(wookiee_people[2])
    clean_han = clean_data(han_solo_data)
    han_solo_data.update(clean_han)
    han_solo = create_person(han_solo_data, wookiee_planets)

    chewie_data = get_swapi_resource('https://swapi.py4e.com/api/people/', params={'search': 'Chewbacca'})['results'][0]
    chewie_data.update(wookiee_people[0])
    clean_chewie = clean_data(chewie_data)
    chewie_data.update(clean_chewie)
    chewie = create_person(chewie_data, wookiee_planets)

    m_falcon_crew = Crew({'pilot': han_solo, 'co-pilot': chewie})
    m_falcon.assign_crew_members(m_falcon_crew)
    m_falcon_passengers = Passengers([rey, finn, bb8])
    m_falcon.add_passengers(m_falcon_passengers)

    filepath_tako = 'stu_episode_vii_journey_takodana.json'
    write_json(filepath_tako, m_falcon.jsonable())

    return endpoint, abs_path
if __name__ == '__main__':
    main()
