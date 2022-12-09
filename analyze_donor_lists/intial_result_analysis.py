from csv_helper import csv_to_dict
import tqdm
import ast
import plotly.express as px

def main():
    results = sort_by_pub(csv_to_dict("/Users/elizabethschwartz/Documents/nonprofit press project/htrc/analyze_donor_lists/results.csv"))
    print('chp', len(results['chp']))
    print('milkweed', len(results['milkweed']))
    print('graywolf', len(results['graywolf']))
    print('new rivers', len(results['new_rivers']))
    chp_donors = []
    graywolf_donors = []
    milkweed_donors = []
    new_rivers_donors = []
    for entry in results['chp']:
        for thing in creates_donor_data(entry):
            chp_donors.append(thing)
    for entry in results['graywolf']:
        for thing in creates_donor_data(entry):
            graywolf_donors.append(thing)
    for entry in results['milkweed']:
        for thing in creates_donor_data(entry):
            milkweed_donors.append(thing)
    for entry in results['new_rivers']:
        for thing in creates_donor_data(entry):
            new_rivers_donors.append(thing)

    print(len(chp_donors))
    print(len(graywolf_donors))
    print(len(milkweed_donors))
    print(len(new_rivers_donors))

    # counts of total donor names
    chp_count = sorted(create_donor_counts(chp_donors), key=get_count,reverse=True)
    graywolf_count = sorted(create_donor_counts(graywolf_donors), key=get_count, reverse=True)
    milkweed_count = sorted(create_donor_counts(milkweed_donors), key=get_count, reverse=True)
    new_rivers_count = sorted(create_donor_counts(new_rivers_donors), key=get_count, reverse=True)
    make_graph(chp_count[0:19], 'Coffee House Press Top 20 Donors')
    make_graph(graywolf_count[0:19], 'Graywolf Press Top 20 Donors')
    make_graph(milkweed_count[0:19], 'Milkweed Editions Top 20 Donors')
    make_graph(new_rivers_count[0:19], 'New Rivers Press Top 20 Donors')




def make_graph(donor_counts, title_text):
    count = []
    donor = []
    for item in donor_counts:
        count.append(item['count'])
        donor.append(item['name'])
    fig = px.bar(x=donor, y=count, title=title_text)

    fig.show()


def get_count(count_dict):
    return count_dict['count']

def create_donor_counts(records):
    donor_names = []
    years = []
    donor_counts = []
    for record in records:
        if record['year'] not in years:
            years.append(record['year'])
        else: pass
    for record in records:
        for year in years:
            if record['year'] == year:
                pass


    for donor_name in donor_names:
        donor_counts.append({'name': donor_name, 'count': 0})
    for record in records:
        for donor_count in donor_counts:
            if record['donor'] == donor_count['name']:
                donor_count['count'] += 1
            else:
                pass
    return donor_counts


def create_donors_per_year(records):
    donor_names = []
    donor_counts = []
    for record in records:
        if record['donor'] not in donor_names:
            donor_names.append(record['donor'])
        else: pass
    for donor_name in donor_names:
        donor_counts.append({'name': donor_name, 'count': 0})
    for record in records:
        for donor_count in donor_counts:
            if record['donor'] == donor_count['name']:
                donor_count['count'] += 1
            else:
                pass
    return donor_counts


def creates_donor_data(record):
    year = int(record['year'])
    donors = []
    these_donors = ast.literal_eval(record['donors'])
    for this_donor in these_donors:
        if this_donor == None:
            pass
        else:
            donors.append({'donor': this_donor, 'year': year})
    return donors




def sort_by_pub(results):
    chp = []
    new_rivers = []
    graywolf = []
    milkweed = []
    for result in tqdm.tqdm(results):
        if result['in_twin_cities'].lower() == "true":
            if result['501c3'].lower() == "true":
                if result['publisher'] == 'Coffee House Press':
                    chp.append(formats_results(result))
                elif result['publisher'] == 'Graywolf Press':
                    graywolf.append(formats_results(result))
                elif result['publisher'] == 'Milkweed Editions':
                    milkweed.append(formats_results(result))
                elif result['publisher'] == 'New Rivers Press':
                    new_rivers.append(formats_results(result))
                else: pass
            else: pass
        else: pass
    return {'chp': chp, 'milkweed': milkweed, 'graywolf': graywolf, 'new_rivers': new_rivers}

def formats_results(record):
    return {'year': record['rights_date_used'], 'htid': record['htid'], 'donors': record['donor_list']}


main()
