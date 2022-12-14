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
#             enter your search terms here -- returns lines with any of the terms provided in the list
            search_terms = ["nonprofit"]
            these_results.append(line_level_concordance_search(infile_name, search_terms, mode="all"))
    makes_results_csv(these_results, "results.csv")



#this version allows for multiple search terms (copyright, donors, foundation, etc.)
def line_level_concordance_search(infile_name, search_term, mode):
    try:
        infile = open(infile_name, 'r')
        # turn the whole thing into one big list
        lines = infile.read().splitlines()
        i = 0
        hits = []
        results = []
        if mode == "any":
            for line in lines:
                if any(a_term.lower() in line.lower() for a_term in search_term):
                    hits.append(i)
                i += 1
        elif mode == "all":
            for line in lines:
                if all(a_term.lower() in line.lower() for a_term in search_term):
                    hits.append(i)
                i += 1
        elif mode == "none":
            for line in lines:
                if not(any(a_term.lower() in line.lower() for a_term in search_term)):
                    hits.append(i)
                i += 1
        else:
            print('enter valid mode value: any, all, or none')
        for hit in hits:
#             adjust the amount of text scraped surrounding the result by changing the lines list index below
            result = (lines[(hit - 5):(hit + 20)])
            results_string = ""
            for item in result:
                results_string = results_string + str(item) + " "
            results_string = re.sub("\\\\", "", results_string)
            results.append({'volume': infile_name.split("/")[1], 'line' : hit, 'text':results_string})
        return results
    except FileNotFoundError:
        pass


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
