#Problem 02
def recieve_treats(trick_or_treaters, candy):
    '''
    Adds the given candy to the treats list of each trick_or_treater

    Parameters:
        trick_or_treaters(dict): a dictionary of trick-or-treaters, candy(str): a string representing a candy

    Returns:
        None
    '''
    values = trick_or_treaters.values()
    for value in values:
        if type(value) == dict: #runs friends_dict
            for bag in value.values():
                if type(bag) == list:
                    bag.append(candy)
        elif type(value) == list: #accounts for individual trick or treaters (patrick)
            value.append(candy)

#Problem 03
def sort_candy(candy_list):
    '''
    Uses the types dict to sort the candies in the candy_list by type

    Parameters:
        candy_list(list): a list of strings, each respresenting a different candy

    Returns:
        dict: types
    '''
    #Setup
    types = {
        'chocolate' : [],
        'fruit' : [],
        'other' : []
    }
    #End Setup
    for candy in candy_list:
        if candy == "hershey bar":
            types['chocolate'].append(candy)
        if candy == "snickers":
            types['chocolate'].append(candy)
        if candy == "skittles":
            types['fruit'].append(candy)
        if candy == "starburst":
            types['fruit'].append(candy)
        if candy == "tootsie roll":
            types['other'].append(candy)
        if candy == 'candy corn':
            types['other'].append(candy)
    return types

def main():
    """
    Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
        None
    """
    #Problem 01
    brian = {
        "costume": "wizard",
        "treats": []
    }
    patrick = {
        "costume": "vampire",
        "treats": []
    }
    simone = {
        "costume": "mummy",
        "treats": []
    }

    friends_dict = {
        "brian": brian,
        "patrick": patrick,
        "simone": simone
    }

    friends_dict_items = friends_dict.items()

    #Problem 02
    recieve_treats(friends_dict, "skittles")
    recieve_treats(friends_dict, "snickers")
    recieve_treats(friends_dict, "candy corn")

    recieve_treats(patrick, "hershey bar")
    recieve_treats(patrick, "starburst")
    recieve_treats(patrick, "tootsie roll")

    #Problem 03
    patricks_candies_sorted = sort_candy(patrick["treats"])
    chocolate_candies = patricks_candies_sorted['chocolate']
    fruit_candies = patricks_candies_sorted['fruit']
    other_candies = patricks_candies_sorted['other']

    return brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies

#Do not modify or delete this line
brian, patrick, simone, friends_dict, friends_dict_items, patricks_candies_sorted, chocolate_candies, fruit_candies, other_candies = main()

#The code below is how main is traditionally called
# if __name__ == '__main__':
#     main()
