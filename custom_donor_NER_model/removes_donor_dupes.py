from makes_donor_lists import csv_to_dict, makes_results_csv
import ast
import re
def main():
    results= csv_to_dict("/Users/elizabethschwartz/Documents/nonprofit press project/htrc/named_entity_experiments/donor_list_results.csv")
    donor_ent_list = []
    for result in results:
        for entity in ast.literal_eval(result['donor_list']):
            stripped_ent = entity.replace('\n', '').replace('-', '').lower()
            stripped_ent = stripped_ent.replace('the', '')
            stripped_ent = re.sub("\s\s+" , " ", stripped_ent).strip()
            donor_ent_list.append({"stripped": stripped_ent, "original": entity})


    deduped_list = []
    for this_ent in donor_ent_list:
        print(this_ent['stripped'])
        if this_ent["stripped"] not in deduped_list:
            deduped_list.append(this_ent['stripped'])
        else:
            print(this_ent['stripped'])

    makes_results_csv(donor_ent_list, 'reduced_name_results.csv')

    # print(donor_ent_list)
    # print(deduped_list)
    print(len(donor_ent_list))
    print(len(deduped_list))

    # makes_results_csv(deduped_list, 'deduped_donors.csv')


def consolidates_names():
    deduped_names = csv_to_dict("/Users/elizabethschwartz/Documents/nonprofit press project/htrc/named_entity_experiments/data/DEDUPED_DONOR_NAMES_2022-11-23-2-56PM.csv")
    authority_names = []
    for name in deduped_names:
        if name['stripped'] not in authority_names:
            authority_names.append(name['stripped'])
        else:
            pass
    results_dict_list = []
    for name in authority_names:
        results_dict_list.append({'authority_name': name, 'aka': []})
    for name in deduped_names:
        for item in results_dict_list:
            if item['authority_name'] == name['stripped']:
                item['aka'].append(name['original'])
            else: pass
    for entry in results_dict_list:
        entry['count'] = len(entry['aka'])


    print(len(results_dict_list))
    makes_results_csv(results_dict_list, 'consolidated_names.csv')


def analyze_cleaned_names(name_file):
    these_donors = csv_to_dict(name_file)
    for entry in these_donors:
        print(entry['authority_name'] + ':', len(entry['aka']))

# main()
consolidates_names()
