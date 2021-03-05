# SI 506 Midterm

def calculate_points_per_game(club):
    """Returns the average number of points earned by a club per game rounded
    to the second decimal place.

    Parameters:
        club (list): club record.

    Returns
        float: average points per game (PPG).
    """

    PPG = round((calculate_points(club) / club[2]), 2)
    return PPG


def calculate_goals_diff(club):
    """Returns the goal difference (GD) between a club's goals for (GF) and
    goals against (GA) per the following equation: GF - GA = GD.

    Parameters:
        club (list): club record.

    Returns
        int: goal difference (GD).
    """
    GD = club[6] - club[7]
    return GD


def calculate_points(club):
    """Returns points (Pts) earned by a club during league plaay. Points are earned as
    follows: 3 points for a win, 1 point for a draw (tie), 0 points for a loss 0.

    Parameters:
        club (list): club record.

    Returns
        int: total points (Pts) earned.
    """

    Pts = (club[3] * 3) + (club[4] * 1) + (club[5] * 0)
    return Pts


def get_clubs_by_regions(clubs, regions):
    """Returns a list of nested club records filtered on a passed in list of one
    or more regions. A region/club match is obtained whenever a club's home
    location is found in a passed in region's tuple of city, county, and/or
    state locations.

    Parameters:
        clubs (list): list of club record lists.
        regions (list): list of regions. Each region contains a tuple of
            cities, counties, and/or states.

    Returns
        list: list of filtered club record lists.
    """
    cbr = []
    for club in clubs:
        for region in regions:
            if club[1] in region[1]:
                cbr.append(club)
    return cbr


def get_top_club_by_ppg(clubs):
    """Returns a formatted string literal representing the top club(s) in the
    league possessing the highest average points per game (PPG) for the season.

    The f-string format is f"< club name > (< points > PPG)".

    If more than one club shares the top PPG, the function will append each
    additional team to the current f-string using the following format:

    f"< top_club > and < club name > (< points > PPG)".

    Parameters:
        clubs (list): list of club record lists.

    Returns
        str: formatted string literal representing the top team(s) by points by game (PPG).
    """

    top_club = None
    points_per_game = 0.0
    for club in clubs:
        if float(club[-1]) > points_per_game:
            top_club = f"{club[0]} ({club[10]} PPG)"
            points_per_game = club[10]
        elif club[-1] == points_per_game:
            top_club = f"{top_club} and {club[0]} ({club[10]} PPG)"
        else:
            continue
    return top_club


def get_words_with_apostrophes(string):
    """Returns a list of tuples of words that include an apostrophe. Each
    tuple in the returned list includes two items: the zero-based word number
    (e.g., 1st word=0, 2nd word=1, nth word=n-1 in the string) and the word
    itself, as in ( < number >, < word >).

    Parameters:
        string (str): the string containing words to be checked for apostrophes.

    Returns
        list: list of tuples.
    """
    words_with_apostrophes = []
    list_of_words = string.split()
    for word in range(len(list_of_words)):
        if "'" in list_of_words[word]:
            x =word, list_of_words[word]
            words_with_apostrophes.append(x)
    return words_with_apostrophes


def search_club_names(clubs, search_term):
    """Returns a list of club record lists filtered on a substring found in the
    club name. Function search is case insensitive.

    Parameters:
        clubs (list): list of club record lists.
        search_term (str): possible substring to be located in a club name.

    Returns
        list: list of club record lists.
    """
    matching_club_names = []
    for club in clubs:
        if search_term.lower() in str(club[0]).lower():
            matching_club_names.append(club)
    return matching_club_names


def main():
    """Program entry point. Controls flow of execution. All function calls must
    be made from main().

    Parameters:
        None

    Returns
        None

    """

    # German states [ < State >, ( < Municipality >, )]
    # Note: Diacritical marks removed from certain names to simplify lookups.
    regions = [
        ['Baden-Wurttemberg', ('Freiberg im Breisgau', 'Hoffenheim', 'Mannheim', 'Willstatt')],
        ['Bavaria', ('Augsburg', 'Ingolstadt', 'Munich', 'Nuremberg')],
        ['Berlin', ('Berlin',)],
        ['Brandenburg', ('Brandenburg an der Havel', 'Cottbus', 'Oranienburg', 'Potsdam')],
        ['Bremen', ('Bremen', 'Bremerhaven')],
        ['Hamburg', ('Hamburg',)],
        ['Hesse', ('Darmstadt', 'Frankfurt am Main', 'Kassel', 'Wiesbaden')],
        ['Lower Saxony', ('Braunschweig', 'Hanover', 'Oldenburg', 'Wolfsburg')],
        ['Mecklenburg-Vorpommern', ('Neubrandenburg', 'Rostock', 'Schwerin', 'Wismar')],
        ['North Rhine-Westphalia', ('Cologne', 'Duisburg', 'Dortmund', 'Essen')],
        ['Rhineland-Palatinate', ('Mainz', 'Ludwigshafen am Rhein', 'Koblenz', 'Trier')],
        ['Saarland', ('Saarbrucken', 'Homburg', 'Volklingen', 'Sankt Ingbert')],
        ['Saxony', ('Chemnitz', 'Dresden', 'Leipzig', 'Zwickau')],
        ['Saxony-Anhalt', ('Halberstadt', 'Magdeburg', 'Stendal', 'Wittenberg')],
        ['Schleswig-Holstein', ('Flensburg', 'Kiel', 'Lubeck', 'Norderstedt')],
        ['Thuringia', ('Erfurt', 'Gera', 'Jena', 'Weimar')]
        ]

    # Frauen-Bundesliga, 2019-2020 season
    # Note: Diacritical marks removed from certain names to simplify lookups.
    clubs = [
        ['USV Jena', 'Jena', 22, 0, 4, 18, 15, 77],
        ['Bayern Munich', 'Munich', 22, 17, 3, 2, 60, 14],
        ['Turbine Potsdam', 'Potsdam', 22, 12, 1, 9, 52, 45],
        ['TSG 1899 Hoffenheim', 'Hoffenheim', 22, 16, 1, 5, 67, 24],
        ['1. FFC Frankfurt', 'Frankfurt am Main', 22, 10, 3, 9, 44, 47],
        ['SC Freiburg', 'Freiberg im Breisgau', 22, 9, 4, 9, 43, 47],
        ['SC Sand', 'Willstatt', 22, 8, 1, 13, 24, 43],
        ['Bayer 04 Leverkusen', 'Cologne', 22, 5, 2, 15, 22, 51],
        ['1. FC Koln', 'Cologne', 22, 5, 2, 15, 22, 60],
        ['MSV Duisburg', 'Duisburg', 22, 4, 5, 13, 19, 47],
        ['SGS Essen', 'Essen', 22, 11, 2, 9, 41, 39, 2],
        ['VfL Wolfsburg', 'Wolfsburg', 22, 20, 2, 0, 93, 8]
        ]

    megan_quote = ("If you miss a shot, you missed it. You can't go back. You can "
    "only try to not make the same mistake twice. I've won a lot in my career, and "
    "I've lost a lot. You take the good with the bad. Also, it's not only about "
    "winning. It's about the process and the journey, the people you're with, "
    "continuing to grow and learn, and getting better every day.")


    # CHALLENGE 01
    club_wdl = clubs[10][3:6]

    print(f"\n01. Sliced club won, draw, loss list = {club_wdl}")


    # CHALLENGE 02

    search_term = '1'
    clubs_by_name =  search_club_names(clubs, search_term)

    print(clubs_by_name)
    print(f"\n02. Clubs = {clubs_by_name}")


    # CHALLENGE 03

    for club in clubs:
        club.append(calculate_goals_diff(club))
        club.append(calculate_points(club))
        club.append(calculate_points_per_game(club))
    print(clubs)
    print(f"\n03. Clubs with GD, Pts, and PPG (n={len(clubs)}) = {clubs}")


    # CHALLENGE 04
    southern_regions = regions[0:2]
    southern_clubs = get_clubs_by_regions(clubs, southern_regions)

    #print(southern_clubs)
    print(f"\n04. Southern clubs (n={len(southern_clubs)}) = {southern_clubs}")


    # CHALLENGE 05
    envelope = [regions[9]]
    north_rhine_clubs = get_clubs_by_regions(regions=envelope, clubs=clubs)

    #print(north_rhine_clubs)
    print(f"\n05. North Rhine-Westphalia (n={len(north_rhine_clubs)}) = {north_rhine_clubs}")


    # CHALLENGE 06

    top_north_rhine_club = get_top_club_by_ppg(north_rhine_clubs)

    print(top_north_rhine_club)
    print(f"\n06. Top North Rhine-Westphalia club(s) = {top_north_rhine_club}")


    # CHALLENGE 07

    words = get_words_with_apostrophes(megan_quote)

    print(words)
    print(f"\n07. Words with apostrophes = {words}")


# Do not modify or delete __name__ check conditional statement.
if __name__ == '__main__':
    main()
