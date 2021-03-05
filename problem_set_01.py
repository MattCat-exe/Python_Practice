# START PROBLEM SET 01
print('Problem Set 01')

# PROBLEM 1 (20 points)
print('\nProblem 1')

#python author = "Guido van Rossum"
#python_author = Guido van Rossum
python_author = "Guido van Rossum"
python_current_version = "3.8.5"
#'3.8.5' = python_version

valid_variables = [python_author , python_current_version]

print(f"\nValid = {valid_variables}")


# PROBLEM 2 (20 points)
print('\nProblem 2')

# PROBLEM 2 SETUP
# Please do not change.

name = "Guido van Rossum"
python_foundation_officers = ['Guido van Rossum', 'Lorena Mesa', 'Thomas Wouters']
zen_of_python = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# END PROBLEM 2 SETUP

type(name)
type(python_foundation_officers)
type(zen_of_python)

name_type = str
officers_type = list
zen_type = str

print(name_type)
print(officers_type)
print(zen_type)

len(zen_of_python)
num_chars_zen =  824

# PROBLEM  3 (20 points)
print('\nProblem 3')
Z = zen_of_python.split()
len(Z)
num_words = 137
avg_words = 137 / 19

print(f"\nNumber of words = {num_words}")
print(f"\nAverage number of words per line = {avg_words}")


# PROBLEM 4 (20 points)
print('\nProblem 4')

total_words = 144.2105263157894735

print(f"\nNew total number of words in Zen of Python = {total_words}")


# PROBLEM 5 (20 points)
print('\nProblem 5')

num_chars_zen = 824

print(f"\nNumber of characters = {num_chars_zen}")

avg_chars = 824 // 137

print(f"\nAverage number of characters per word = {avg_chars}")