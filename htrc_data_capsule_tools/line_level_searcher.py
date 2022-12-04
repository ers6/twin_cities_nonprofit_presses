import csv
import os
import re

def main():
    directory = 'workset/'
    these_results = []
    for subdir in os.listdir(directory):
        f = os.path.join(directory, subdir)
        print(f)
        if os.path.isdir(f):
            print(f)
            file_name = f.split('/')[1]
            infile_name = str(f)+"/"+file_name +".txt"
            search_terms = ["nonprofit"]
            these_results.append(line_level_concordance_search(infile_name, search_terms))
    print(these_results)
    makes_results_csv(these_results, "results_refac.csv")


# deprecated version of gets funding data that returns results as a list of strings instead of a massive string
#this version allows for multiple search terms (copyright, donors, foundation, etc.)
def line_level_concordance_search(infile_name, search_term):
    try:
        infile = open(infile_name, 'r')
        # turn the whole thing into one big list
        lines = infile.read().splitlines()
        i = 0
        hits = []
        results = []
        for line in lines:
            if any(a_term.lower() in line.lower() for a_term in search_term):
                print('found in line:', i, line)
                hits.append(i)
            i += 1
        print(hits)
        for hit in hits:
            print(lines[(hit - 5):(hit + 20)])
            result = (lines[(hit - 5):(hit + 20)])
            results_string = ""
            for item in result:
                results_string = results_string + str(item) + " "
            results_string = re.sub("\\\\", "", results_string)
            results.append({'volume': infile_name.split("/")[1], 'line' : hit, 'text':results_string})
        headers = ['volume','line', 'text']
        rows = results
        return rows
    except FileNotFoundError:
        pass


# def gets_funding_data(infile_name, search_term):
#     try:
#         infile = open(infile_name, 'r')
#         print('howdy')
#         lines = infile.read().splitlines()
#         i = 0
#         hits = []
#         results = []
#         for line in lines:
#             if search_term.lower() in line.lower():
#                 print('found in line:', i, line)
#                 hits.append(i)
#                 i += 1
#         print(hits)
#         for hit in hits:
#             print(lines[(hit - 10):(hit + 10)])
#             result = (lines[(hit - 5):(hit + 5)])
#             result_string = ""
#             for item in result:
#                 result_string = result_string + " " + item
#             result_string = re.sub("\\\\", "", result_string)
#             htid = infile_name.split("/")[1]
#             results.append({'volume': htid, 'line' : hit, 'text':result_string})
#             headers = ['volume','line', 'text']
#             rows = results
#             return rows
#     except FileNotFoundError:
#         print(infile_name, "could not be found")



def makes_results_csv(results, outfile_name):
    headers = ['volume', 'line', 'text']
    rows = results
    for row in rows:
        if row == None:
            rows.remove(row)
    print(type(rows))
    with open(outfile_name, 'w', encoding='UTF-8', newline= '') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerows(row)
            except TypeError:
                pass


main()