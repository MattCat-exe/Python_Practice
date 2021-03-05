# START PROBLEM SET 04
print('Problem Set 04')

# START SET UP
summary = [
    'Step 1: Beat It',
    'Step 2: Prep the Pan',
    'Step 3: Add the Eggs',
    'Step 4: Patience Makes Perfect',
    'Step 5: Almost Done',
    'Step 6: Ready to Eat'
]
recipe = [
    "Beat your eggs until they're completely blended. Add a little water, cream or milk to make them tender. Use 1 tablespoon of liquid per egg. Add a pinch of salt.",
    "Next, heat a nonstick skillet over a medium-low flame and toss in a pat of butter. Make sure the butter coats the pan.",
    "Then, pour in the eggs. Pause to let them heat slightly — gentle heat is essential.",
    "Move the eggs across the pan like a bulldozer so the eggs cook evenly. This takes a little time, but it's worth it.",
    "As the eggs start to set, add chopped fresh herbs, or bits of ham or cheese.",
    "Turn your eggs onto warmed plates and dig in! Watch our how-to video for more."
]

# Problem 01
print('\nProblem 1')

#1.1
step_length = [] #accumulator_3000
for i in recipe:
    char_num = len(i)
    step_length.append(char_num)

#1.2
gte_100 = 0
less_100 = 0
for each in step_length:
    if each > 100:
        gte_100 += 1
    if each < 100:
        less_100 += 1

#1.3
step_25_mins = 0
for minute in step_length[1:5]:
    if minute > 100:
        step_25_mins += 10
    else:
        step_25_mins += 5

# Problem 02
print('\nProblem 2')
#2.1

step_order_3 = ((summary[2][0:4]).upper()) + ('3')


#2.2
recipe_summary_3 = f"{step_order_3}: {recipe[2]}"

#2.3
recipe_summary = []
for each in range(len(summary)):
    recipe_summary.append(f"{summary[each][:4].upper()}{each+1}: {recipe[each]}")


# Problem 03
print('\nProblem 3')
#3.1
step2_r_num = 0
for each_character in recipe[1]:
    if each_character == 'r':
        step2_r_num = step2_r_num + 1

#3.2
step_r_num = []

for letter_r in recipe:
    step_r_num.append(letter_r.count("r"))

#3.3
max_r_num = 0
max_r_index = 0
prev_r_count = 0
for each in step_r_num:
    if each > prev_r_count:
        max_r_num = each
        max_r_index = step_r_num.index(each)
        prev_r_count = each #reset
    else:
        continue