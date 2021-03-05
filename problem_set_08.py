# START PROBLEM SET 08 
print('Problem set 08 \n')

# SETUP
import csv

state2state_id = {
    'Alabama' : 'AL',
    'Alaska' : 'AK',
    'Arizona' : 'AZ',
    'Arkansas' : 'AR',
    'California' : 'CA',
    'Colorado' : 'CO',
    'Connecticut' : 'CT',
    'Delaware' : 'DE',
    'Florida' : 'FL',
    'Georgia' : 'GA',
    'Hawaii' : 'HI',
    'Idaho' : 'ID',
    'Illinois' : 'IL',
    'Indiana' : 'IN',
    'Iowa' : 'IA',
    'Kansas' : 'KS',
    'Kentucky' : 'KY',
    'Louisiana' : 'LA',
    'Maine' : 'ME',
    'Maryland' : 'MD',
    'Massachusetts' : 'MA',
    'Michigan' : 'MI',
    'Minnesota' : 'MN',
    'Mississippi' : 'MS',
    'Missouri' : 'MO',
    'Montana' : 'MT',
    'Nebraska' : 'NE',
    'Nevada' : 'NV',
    'New Hampshire' : 'NH',
    'New Jersey' : 'NJ',
    'New Mexico' : 'NM',
    'New York' : 'NY',
    'North Carolina' : 'NC',
    'North Dakota' : 'ND',
    'Ohio' : 'OH',
    'Oklahoma' : 'OK',
    'Oregon' : 'OR',
    'Pennsylvania' : 'PA',
    'Rhode Island' : 'RI',
    'South Carolina' : 'SC',
    'South Dakota' : 'SD',
    'Tennessee' : 'TN',
    'Texas' : 'TX',
    'Utah' : 'UT',
    'Vermont' : 'VT',
    'Virginia' : 'VA',
    'Washington' : 'WA',
    'West Virginia' : 'WV',
    'Wisconsin' : 'WI',
    'Wyoming' : 'WY'
}

# END SETUP



### PROBLEM 1.1
def read_txt(filepath):
    """Returns a list of lists where each item (list) is formed from the data split by tab.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of lists that contain states and total number of cases
    """
    txt_list = []
    with open (filepath, 'r', encoding='utf-8') as file_obj:
        data = file_obj.readlines()
        for info in data[1:]:
            info = info.strip('\n')
            txt_list.append(info.split('\t'))
        return txt_list

### PROBLEM 1.2
def read_csv(filepath):
    """Returns a list of dictionaries where each dictionary is formed from the data.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of dictionaries where each dictionary is formed from the data
    """
    with open (filepath, 'r', encoding='utf-8') as file_obj:
        data = []
        reader = csv.DictReader(file_obj)
        for line in reader:
            data.append(dict(line))
        return data



### PROBLEM 2
def convert_to_dict(data):
    """Returns a dictionary of US state and the total number of COVID-19 cases as key-value pairs.

    Parameters:
        data (list): a list of lists that contain states and total number of cases
    
    Returns:
        dict: a dictionary that contains state and the total number of cases as key-value pairs
    """
    new_dict = {}
    for state in data:
        new_dict[state[0]] = state[1]
    return new_dict


### PROBLEM 3
def get_total_num_policies(data):
    """Returns a dictionary of US state id and the total number of state-level policies as key-value pairs.

    Parameters:
        data (list): a list of dictionaries where each dictionary is formed from the data.
    
    Returns:
        state_id_2_policy_counts (dict): a dictionary of US state id and the total number of state-level policies as key-value pairs
    """
    state_id_2policies = {}
    for policy in data:
        if policy['state_id'] not in state_id_2policies.keys():
            state_id_2policies[policy['state_id']] = 0
        if policy['policy_level'] == 'state':
            if policy['start_stop'] == 'start':
                state_id_2policies[policy['state_id']] += 1
    
    return state_id_2policies


### PROBLEM 4
def summarize_data(state2state_id, state_id_2_policy_counts, state2cases):
    """Returns a list of dictionaries that contain four key-value pairs: US state, US state id, the total number of state-level policies, and the total number of COVID-19 cases.
    
    Keys are state, state_id, total_policies, and total_cases.

    Parameters:
        three dictionaries: 
            state2state_id is a dictionary of state names and their ids as key-value pairs
            state_id_2_policy_counts is a dictionary of US state id and the total number of state-level policies as key-value pairs
            state_2_case_counts is a dictionary of US state and the total number of COVID-19 cases as key-value pairs
    
    Returns:
        data (list): a list of dictionaries with four key-value pairs.
    """
    working_list = []
    for state_name in state2state_id.keys():
        state_dict = {'state': state_name, 'state_id': state2state_id[state_name]}
        state_dict['total_policies'] = state_id_2_policy_counts[state_dict['state_id']]
        state_dict['total_cases'] = state2cases[state_dict['state']]
        working_list.append(state_dict)
    return working_list


### PROBLEM 5
def write_csv(data, filepath):
    """Writes a csv file from an input data given a filepath.
    
    Parameters:
        data (list): a list of dictionaries with state, state_id, the total number of state-level policies, and the total number of COVID-19 cases.
        filepath (str):  a filepath to store data to a csv file.
    
    Returns:
        None
    """
    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(data[0])
        for entry in data[0:]:
            writer.writerow(entry.values())

def main():
    """Program entry point.  Handles program workflow (or words to that effect).

    Parameters:
        None

    Returns:
       None
    """
    #Filepaths
    US_Covid_Cases = '/Users/matthenning/Documents/umich/courses/SI506/assignments/PS/PS_08/us_covid19_cases.txt'
    Policy_Updates = '/Users/matthenning/Documents/umich/courses/SI506/assignments/PS/PS_08/us_policy_updates.csv'
    csv_output = '/Users/matthenning/Documents/umich/courses/SI506/assignments/PS/PS_08/state_covid19_related_info.csv'
    
    ### Problem 1 (20 points)
    cases = read_txt(US_Covid_Cases)
    #print(cases)
    policies = read_csv(Policy_Updates)
    #print(policies)
    ### Problem 2 (10 points)
    state2cases = convert_to_dict(cases)
    #print(state2cases)
    ### Problem 3 (30 points)
    state_id2policies = get_total_num_policies(policies)
    #print(state_id2policies)
    ### Problem 4 (30 points)
    summarized_info = summarize_data(state2state_id, state_id2policies, state2cases)
    #print(summarized_info[1])
    ### Problem 5 (10 points)
    write_csv(summarized_info, csv_output)
#Do not delete the lines below.
if __name__ == '__main__':
    main()
