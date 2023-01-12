def avg_value(value_list):
    average = sum(value_list)/len(value_list)
    return average

def avg_group(table, field):
    field_values = set(table[field].values())
    avg_dictionary = dict()

    for value in field_values:
        total_bills = [v for k, v in table['total_bill'].items() if table[field][k] == value]
        tips = [v for k, v in table['tip'].items() if table[field][k] == value]
        sizes = [v for k, v in table['size'].items() if table[field][k] == value]
        avg_dictionary[value] = [avg_value(total_bills), avg_value(tips), avg_value(sizes)]
    
    return avg_dictionary

d = {
    'total_bill': {69: 15.01, 103: 22.42, 84: 15.98, 207: 38.73, 0: 16.99},
    'tip': {69: 2.09, 103: 3.48, 84: 2.03, 207: 3.0, 0: 1.01},
    'sex': {69: 'Male', 103: 'Female', 84: 'Male', 207: 'Male', 0: 'Female'},
    'smoker': {69: 'Yes', 103: 'Yes', 84: 'No', 207: 'Yes', 0: 'No'},
    'day': {69: 'Sat', 103: 'Sat', 84: 'Thur', 207: 'Sat', 0: 'Sun'},
    'time': {69: 'Dinner', 103: 'Dinner', 84: 'Lunch', 207: 'Dinner', 0: 'Dinner'},
    'size': {69: 2, 103: 2, 84: 2, 207: 4, 0: 2}
}

        
sex_averages = avg_group(d, 'sex')
sex_results = {'Female': [19.705, 2.245, 2.0], 'Male': [23.24, 2.373333333333333, 2.6666666666666665]}
sex_averages == sex_results

