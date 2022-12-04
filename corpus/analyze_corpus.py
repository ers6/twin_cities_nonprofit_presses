import csv
import json
import tqdm

def main(): 
    with open("metadata.json") as json_file:
        collection_metadata = json.load(json_file)["gathers"]
    collection_metadata = in_twin_cities(if_501c3(analyzes_vol_metadata(collection_metadata)))
    writes_report(collection_metadata, "report.txt")
    the_results = []
    for item in collection_metadata:
        for entry in collection_metadata[item]:
            the_results.append(entry)
    print(len(the_results))
    makes_results_json(the_results, "suplemented_collection_metadata.json")
    

def writes_report(metadata, outfile): 
    chp_501c3 = []
    graywolf_501c3 = []
    milkweed_501c3 = []
    new_rivers_501c3 = []
    for book in tqdm.tqdm(metadata['chp']):
        if book['501c3']: 
            chp_501c3.append(book)
        else: pass
    for book in metadata['graywolf']:
        if book['501c3']: 
            graywolf_501c3.append(book)
        else: pass
    for book in metadata['milkweed']:
        if book['501c3']: 
            milkweed_501c3.append(book)
        else: pass
    for book in metadata['new_rivers']:
        if book['501c3']: 
            new_rivers_501c3.append(book)
        else: pass
    with open(outfile, 'w') as the_file: 
        total_records = len(metadata['chp']) + len(metadata['graywolf']) + len(metadata['milkweed']) + len(metadata['new_rivers'])
        print('there were', total_records, 'records total', file=the_file)
        print('---CHP---', file=the_file)
        print('there were', len(metadata['chp']), 'CHP books.', file=the_file)
        print('of these', len(chp_501c3), 'were published when chp was a 501c3 in MN', file=the_file)
        print('---GRAYWOLF---', file=the_file)
        print('there were', len(metadata['graywolf']), 'graywolf books.', file=the_file)
        print('of these', len(graywolf_501c3), 'were published when Graywolf was a 501c3 in MN', file=the_file)
        print('---MILKWEED---', file=the_file)
        print('there were', len(metadata['milkweed']), 'milkweed books.', file=the_file)
        print('of these', len(milkweed_501c3), 'were published when Milkweed was a 501c3 in MN', file=the_file)
        print('---NEW RIVERS---', file=the_file)
        print('there were', len(metadata['new_rivers']), 'new rivers books.', file=the_file)
        print('of these', len(new_rivers_501c3), 'were published when new rivers was a 501c3 in MN', file=the_file)


def adds_address(metadata_collection): 
    # adds address for presses when known
    for book in metadata_collection['chp']: 
        if book['rights_date_used'] == 1984:
            book['pub_location'] = {"address": "626 E. Main Street, West Branch, Iowa", "lat": "", "long": ""}
        elif book['rights_date_used'] >= 1985 and book['rights_date_used'] <= 1988:
            book['pub_location'] = {"address": "24 N. 3rd street, Minneapolis, Minnesota", "lat": 44.98214, "long": -93.27077}
        elif book['rights_date_used'] >= 1989 and book['rights_date_used'] <= 2007:
            book['pub_location'] = {"address" : "27 N. 4th street, Minneapolis, Minnesota", "lat": 44.98088, "long": -93.27247}
        elif book['rights_date_used'] > 2007 and book['rights_date_used'] < 2023: 
            book['pub_location'] = {"address" : "79 Thirteenth Avenue NE, suite 110, Minneapolis, Minnesota", "lat": 45.00008053541784, "long": -93.27116988649234}
        else: pass
    

def if_501c3(metadata_collection): 
    # chp became a 501c3 nonprofit in 1984, the same year it was founded. prior to that
    # chp was called Toothpaste Press and operated in West Branch, Iowa
    for book in metadata_collection['chp']:
        if book['rights_date_used'] >= 1984 and book['rights_date_used'] <= 2023:
            book['501c3'] = True
        else:
            book['501c3'] = False
    # milkweed chronicle incorporated as a nonprofit in 1979
    for book in metadata_collection['milkweed']:
        if book['rights_date_used'] >= 1979 and book['rights_date_used'] <= 2023:
            book['501c3'] = True
        else:
            book['501c3'] = False
    # graywolf became a MN nonprofit in 1985, but it was probably a nonprofit in WA before this 
    for book in metadata_collection['graywolf']:
        if book['rights_date_used'] >= 1985 and book['rights_date_used'] <= 2023:
            book['501c3'] = True
        else:
            book['501c3'] = False
    # new rivers gains 501c3 nonprofit status in 1982  
    for book in metadata_collection['new_rivers']:
        if book['rights_date_used'] >= 1982 and book['rights_date_used'] <= 2001:
            book['501c3'] = True
        else:
            book['501c3'] = False
    return metadata_collection


def in_twin_cities(metadata_collection): 
    # chp became a 501c3 nonprofit in MN in 1984; however, the Kornblums likely did not move to the Twin Cities until
    # 1985 
    for book in metadata_collection['chp']:
        if book['rights_date_used'] >= 1985 and book['rights_date_used'] <= 2023:
            book['in_twin_cities'] = True
        else:
            book['in_twin_cities'] = False
    # milkweed has been in the Twin Cities since its 1979 founding. 
    for book in metadata_collection['milkweed']:
        if book['rights_date_used'] >= 1979 and book['rights_date_used'] <= 2023:
            book['in_twin_cities'] = True
        else:
            book['in_twin_cities'] = False
    # graywolf moved from Port Townsend, WA to St. Paul in 1985
    for book in metadata_collection['graywolf']:
        if book['rights_date_used'] >= 1985 and book['rights_date_used'] <= 2023:
            book['in_twin_cities'] = True
        else:
            book['in_twin_cities'] = False
    # New Rivers moved to St Paul in 1977
    for book in metadata_collection['new_rivers']:
        if book['rights_date_used'] >= 1977 and book['rights_date_used'] <= 2001:
            book['in_twin_cities'] = True
        else:
            book['in_twin_cities'] = False
    return metadata_collection
    
    




def csv_to_dict(csv_file_name):
    results = []
    with open(csv_file_name, 'r', newline='', encoding='utf-8') as infile:
        csvin = csv.reader(infile)
        headers = next(csvin)
        # Make headers str.lower
        headers = [header.strip().lower() for header in headers]
        # Save dictionary of header:value for each row of data
        for row in csvin:
            n = 0
            your_dict = {}
            for column in row:
                your_dict[headers[n]] = column
                n += 1
            results.append(your_dict)
    return results


def analyzes_vol_metadata(metadata_collection):
    chp = []
    new_rivers = []
    milkweed = []
    graywolf = []
    errors = []
    total_results = []
    for record in metadata_collection:

        publisher = gets_publisher(record["imprint"])

        if publisher == "Graywolf Press":
            record['publisher'] = "Graywolf Press"
            graywolf.append(record)
        elif publisher == "Coffee House Press":
            record['publisher'] = "Coffee House Press"
            chp.append(record)
        elif publisher == "Milkweed Editions":
            record['publisher'] = "Milkweed Editions"
            milkweed.append(record)
        elif publisher == "New Rivers Press":
            record['publisher'] = "New Rivers Press"
            new_rivers.append(record)
        else:
            errors.append(record)
    results_dict = {"chp": chp, "new_rivers": new_rivers, "milkweed": milkweed, "graywolf": graywolf}
    # print(results_dict)
    return results_dict


def gets_publisher(imprint_metadata):
    # print(imprint_metadata)
    if "graywolf" in str(imprint_metadata).lower().strip():
        return "Graywolf Press"
    elif "coffee house press" in str(imprint_metadata).lower().strip():
        return "Coffee House Press"
    elif "milkweed editions" in str(imprint_metadata).lower().strip():
        return "Milkweed Editions"
    elif "new rivers" in str(imprint_metadata).lower().strip():
        return "New Rivers Press"
    else:
        pass
        # print("something went wrong")
        # print(imprint_metadata)


def makes_results_json(results, outfile_name):
    json_results = json.dumps(results)
    with open(outfile_name, "w") as outfile:
        outfile.write(json_results)


main()
