# START PROBLEM SET O5
print('Problem Set 05')

# Problem 01
print('\nProblem 1')

# SETUP
def count_vowels(word):
    lower_word = word.lower()
    num_a = lower_word.count("a")
    num_e = lower_word.count("e")
    num_i = lower_word.count("i")
    num_o = lower_word.count("o")
    num_u = lower_word.count("u")
    total_vowels = num_a + num_e + num_i + num_o + num_u
    return total_vowels

example_words = ["Scrabble",
"puppies",
"kittens",
"mellifluous",
"Supercalifragilisticexpialidocious"
]
# END SETUP

callously_score = count_vowels('callously')

example_words_score = 0
for i in example_words:
    res =  count_vowels(i)
    example_words_score =+ example_words_score + res

## PROBLEM 2
print('\nProblem 2')

def score_list(word_list):
    rs = 0
    for i in word_list:
        rs =+ rs + count_vowels(i)
    return rs


## PROBLEM 3
print('\nProblem 3')

def who_wins(player1_score, player2_score):
    if player1_score > player2_score:
        result = "Player 1 wins! Yay!"
    elif player2_score > player1_score:
        result = "Player 2 wins! Boo."
    elif player1_score == player2_score:
        result = "It was a tie! Well that's boring."
    return result

## PROBLEM 4
print('\nProblem 4')

def play_blinkbot_scrabble(list_player1_words, list_player2_words):
    p1 = score_list(list_player1_words)
    p2 = score_list(list_player2_words)
    result = who_wins(p1, p2)
    return result



## PROBLEM 5

# SETUP
def how_much_sleep(hours_slept):
    hours_left = 8 - hours_slept
    if hours_left >= 0:
        return hours_left
    else:
        return 0
# END SETUP

# COMPLETE THE FOLLOWING DOCUMENTATION
'''
Function name: how_much_sleep

Explanation:
    This function calculates how much sleep the chatbot has left to sleep.
    The chatbot is supposed to sleep 8 hours a day; if the chatbot has slept fewer hours,
    the function will state how many hours the chatbot has left to sleep.

Parameters: hours_slept, an integer representing the hours slept

Returns: An integer representing how many more hours Blinkbot should sleep in order to get to 8

'''