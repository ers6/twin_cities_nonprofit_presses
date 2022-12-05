from csv_helper import csv_to_dict, makes_results_csv
import ast

def main():
    ent_name_key = csv_to_dict("authority_name_keys.csv")
    full_results = csv_to_dict("full_results.csv")
    normalized_donor_lists = []
    for this_result in full_results:
        donor_list = []
        for this_donor in ast.literal_eval(this_result['processed_list']):
            donor_list.append(matches_auth_name(this_donor, ent_name_key))
        normalized_donor_lists.append({'htid': this_result['volume'], 'donors': donor_list})
    print(type(normalized_donor_lists[0]))
    makes_results_csv(normalized_donor_lists, 'normalized_donor_list.csv')

def matches_auth_name(donor_name, ent_keys):
    for a_key in ent_keys:
        if donor_name in a_key['aka'].split('||'):
            return a_key['authority_name']
        else:
            pass


main()
