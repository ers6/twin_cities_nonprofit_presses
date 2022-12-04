# runs the spacy model over the entire data set and returns a csv file with htids and donor lists
import csv
import spacy
import tqdm

def main():
    nlp = spacy.load("/Users/elizabethschwartz/Desktop/content/model-best")
    results = csv_to_dict("/Users/elizabethschwartz/Documents/nonprofit press project/named_entity_experiments/data/full_results.csv")
    for entry in tqdm.tqdm(results):
        donor_list = []
        doc = nlp(entry['text'])
        for ent in doc.ents:
            donor_list.append(ent.text)
        entry['donor_list'] = donor_list

    makes_results_csv(results, 'donor_list_results.csv')

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

def makes_results_csv(results, outfile_name):
    headers = results[0].keys()
    rows = results
    print(rows)
    with open(outfile_name, 'w', encoding='UTF-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            # print(row)
            # print('this is type row', type(row))
            # print(row.keys())
            try:
                writer.writerow(row)
            except AttributeError:
                pass


# main()