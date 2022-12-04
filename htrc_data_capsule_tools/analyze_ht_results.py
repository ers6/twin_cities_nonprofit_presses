import csv
import re
import requests
import json
#INPUT:
# -----a csv file from a data capsule with 3 columns (ht_id, line, text)
# -----JSON file of the collection metadata for the collection from which the volumes were downloaded
# OUTPUT:
# ----report.txt file that contains a report of how many volumes were in the collection, how many downloaded, and
#     and which htids (vols) we don't have results for
# ----csv file of results plus metadata from JSON file
# USE: use this python program to figure out how many results are missing, get a list of those missing results, and
#      supplement a csv file of results with available metadata

def main():
    # actual program should prompt for these file paths :)
    dc_results_file =  "/complete/path/to/results.csv"
    collection_metadata_file = "/complete/path/to/collection_metadata.json"
    # turns the files into useable python data types
    with open(collection_metadata_file) as json_file:
        collection_metadata = json.load(json_file)["gathers"]
    dc_results = csv_to_dict(dc_results_file)
    unique_result_vol = []
    total_results = []

    for entry in collection_metadata:
        for result in dc_results:
            if result["volume"] == entry["htid"]:
                total_results.append({"volume": result["volume"], "line": result["line"], "text": result["text"],
                                      "title": entry["title"], "imprint": entry["imprint"], "author": entry["author"],
                                      "pub_date": entry["rights_date_used"], "pub_place": entry["pub_place"],
                                      "ht_bib_key":entry["ht_bib_key"], "oclc_num": entry["oclc_num"], "isbn": entry["isbn"],
                                      "lccn": entry["lccn"], "from_library": entry["content_provider_code"],
                                      "digitized_by": entry["digitization_agent_code"], "ht_catalog_url": entry['catalog_url'],
                                      "ht_handle": entry["handle_url"]})
                if result["volume"] not in unique_result_vol:
                    unique_result_vol.append(result["volume"])
                else:
                    pass
    collection_report_dict = analyzes_vol_metadata(collection_metadata)
  
    # create results csv from collection_report_dict here
    print(total_results)
    makes_results_csv(total_results, "results.csv")
    make_collection_report(collection_report_dict, collection_metadata, total_results, unique_result_vol, outfile_name="report.txt" )


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
            graywolf.append(record)
        elif publisher == "Coffee House Press":
            chp.append(record)
        elif publisher == "Milkweed Editions":
            milkweed.append(record)
        elif publisher == "New Rivers Press":
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

def unique_vols_by_publisher(results_list, publisher_name, metadata_collection, outfile):
    books = []
    for vol in results_list:
        print(vol)
        try:
            get_volume_metadata(vol, metadata_collection)
        #     where we need to start creating the output csv file!!!!
        except TypeError:
            pass
        if gets_publisher(vol["imprint"]) == str(publisher_name):
            books.append(vol["volume"])
    unique_books = []
    for book in books:
        if book not in unique_books:
            unique_books.append(book)
    print("there are", len(books), publisher_name, "results. There are", len(unique_books), "unique titles.", file=outfile)
    return unique_books

def find_missing_titles(results_list, collection_list):
    missing = []
    htids = []
    records = collection_list
    for record in records:
        htids.append(record["htid"])

    for htid in htids:
        if htid not in results_list:
            missing.append(htid)
    return missing


def get_volume_metadata(this_result, collection_metdata):
    for entry in collection_metdata:
        if entry["htid"] == this_result["volume"]:
            this_result["title"] = entry["title"]
            this_result["imprint"] = entry["imprint"]
            this_result["author"] = entry["author"]
            this_result["pub_date"] = entry["rights_date_used"]
            # this_result["pub_date"] = entry["pub_date"]
            this_result["pub_place"] = entry["pub_place"]
            this_result["ht_bib_key"] = entry["ht_bib_key"]
            this_result["oclc_num"] = entry["oclc_num"]
            this_result["isbn"] = entry["isbn"]
            this_result["lccn"] = entry["lccn"]
            this_result["from_library"] = entry["content_provider_code"]
            # this_result["from_library"] = entry["from_library"]
            this_result["digitized_by"] = entry["digitization_agent_code"]
            # this_result["digitized_by"] = entry["digitized_by"]
            this_result["ht_catalog_url"] = entry['catalog_url']
            # this_result["ht_catalog_url"] = entry['ht_catalog_url']
            this_result["ht_handle"] = entry["handle_url"]
            # this_result["ht_handle"] = entry["ht_handle"]
            # print(this_result)
            return this_result
        else:
            pass

# customize the collection report for your purposes!
def make_collection_report(collection_report_dict, collection_metadata, total_results, unique_result_vol, outfile_name):
    outfile = open(outfile_name, "w", encoding="utf-8")
    print("COLLECTION WIDE REPORT:", file=outfile)
    print("there are", len(total_results), "total results", file=outfile)
    print("from", len(unique_result_vol), "total volumes", file=outfile)
    print("there should have been", len(collection_metadata), "unique volumes total.", file=outfile)
    print("\n", file=outfile)
    print("COFFEE HOUSE PRESS REPORT:", file=outfile)
    print("there are", len(collection_report_dict["chp"]), "books by coffee house in the collection", file=outfile)
    unique_chp = unique_vols_by_publisher(total_results, "Coffee House Press", collection_metadata, outfile)
    missing_chp = find_missing_titles(unique_chp, collection_report_dict["chp"])
    print("there are", len(missing_chp), "missing titles:", missing_chp, file=outfile)
    print("\n", file=outfile)

    print("MILKWEED EDITIONS REPORT:", file=outfile)
    print("there are", len(collection_report_dict["milkweed"]), "books by milkweed in the collection", file=outfile)
    unique_milkweed = unique_vols_by_publisher(total_results, "Milkweed Editions", collection_metadata, outfile)
    missing_milkweed = find_missing_titles(unique_milkweed, collection_report_dict["milkweed"])
    print("there are", len(missing_milkweed), "missing titles:", missing_milkweed, file=outfile)
    print("\n", file=outfile)

    print("GRAYWOLF PRESS REPORT:", file=outfile)
    print("there are", len(collection_report_dict["graywolf"]), "books by graywolf in the collection", file=outfile)
    unique_graywolf = unique_vols_by_publisher(total_results, "Graywolf Press", collection_metadata, outfile)
    missing_graywolf = find_missing_titles(unique_graywolf, collection_report_dict["graywolf"])
    print("there are", len(missing_graywolf), "missing titles:", missing_graywolf, file=outfile)
    print("\n", file=outfile)

    print("NEW RIVERS PRESS REPORT:", file=outfile)
    print("there are", len(collection_report_dict["new_rivers"]), "books by new rivers in the collection", file=outfile)
    unique_new_rivers = unique_vols_by_publisher(total_results, "New Rivers Press", collection_metadata, outfile)
    missing_newriv = find_missing_titles(unique_new_rivers, collection_report_dict["new_rivers"])
    print("there are", len(missing_newriv), "missing titles:", missing_newriv, file=outfile)


def makes_results_csv(results, outfile_name):
    headers = ['volume', 'line', 'text', "title", "imprint", 'author', 'pub_date', 'pub_place', 'ht_bib_key', 'oclc_num', 'isbn','lccn', 'from_library', 'digitized_by', 'ht_catalog_url', 'ht_handle']
    rows = results
    print(rows)
    with open(outfile_name, 'w', encoding='UTF-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except AttributeError:
                pass



main()
