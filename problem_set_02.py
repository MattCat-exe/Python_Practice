# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (20 points)
print('\nProblem 1')

cases = [11, 10, 38, 19, 27]

cases_latest = cases[-1] #Assign
cases[0] = 9
#print(cases)
# PROBLEM 2 (20 points)
print('\nProblem 2')

tests = [] #Assign
tests.append(867)
tests.append(854)
tests.append(1494)
tests.append(1712)
tests.append(1667)

tests_max = max(tests) #Assign

tests_max_index = 3 #Assign


# PROBLEM 3 (20 points)
print('\nProblem 3')

weeks = ' Aug.09,Aug.16,Aug.23,Aug.30,Sep.06 '
weeks_expanded = " ".join(weeks)
weeks_expanded_list = weeks_expanded.split()
weeks_expanded_list.remove('.')
weeks_expanded_list.remove('.')
weeks_expanded_list.remove('.')
weeks_expanded_list.remove('.')
weeks_expanded_list.remove('.')
weeks_list_string = ''.join(weeks_expanded_list)
weeks_list_string.strip()
updated_weeks_list = weeks_list_string.split(',')
''.join(updated_weeks_list)
print(updated_weeks_list)
#print(updated_weeks_list)
weeks_list = updated_weeks_list #Assign

# PROBLEM 4 (20 points)
print('\nProblem 4')

weeks_new = '|'.join(weeks_list) #Assign
aug_count = weeks_new.count('Aug') #Assign

# PROBLEM 5 (20 points)
print('\nProblem 5')
weeks_list_var = weeks_list[3]
test_num_var = tests[3]
case_num_var = cases[3]
most_tests = (f"In the week starting on {weeks_list_var}, UM has conducted {test_num_var} tests and reported {case_num_var} cases.") #Assign
#print(most_tests)
weeks_list_var_2 = weeks_list[2]
test_num_var_2 = tests[2]
case_num_var_2 = cases[2]
most_cases = (f"In the week starting on {weeks_list_var_2}, UM has conducted {test_num_var_2} tests and reported {case_num_var_2} cases.") #Assign
#print(most_cases)