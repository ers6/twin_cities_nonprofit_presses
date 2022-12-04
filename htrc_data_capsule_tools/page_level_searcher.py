import os
import csv

def main():
    directory = "/workset"
    results = []
    for subdir in os.listdir(directory):
        volume_download_file = os.path.join(directory, subdir)
        if os.path.isdir(volume_download_file):
            for volume in os.listdir(volume_download_file):
                vol_path = volume_download_file + '/' +volume
                if os.path.isdir(vol_path):
                    for page_file in os.listdir(vol_path):
                        with open(vol_path + '/'+ page_file, 'r') as page:
                            text = page.read()
#                             input your search terms here!!!
                            found = page_level_concordance_search(text, ['whale', 'and'], mode='all')
                            if found:
                                results.append({'volume': str(volume_download_file.split('/')[-1]),'page': str(page_file.split('.')[0]), 'text' : text})
            makes_results_csv(results, 'the-results.csv')


def page_level_concordance_search(page_text, search_terms, mode):
    if mode == 'any':
        if any(a_term.lower() in page_text.lower() for a_term in search_terms):
            return True
        else:
            return False
    elif mode == 'all':
        if all(a_term.lower() in page_text.lower() for a_term in search_terms):
            return True
        else:
            return False
    elif mode == 'none':
        if not (any(a_term.lower() in page_text.lower() for a_term in search_terms)):
            return True
        else:
            return False
    else:
        print('enter valid mode value: any, all, or none')


def makes_results_csv(results, outfile_name):
    headers = ['volume', 'page', 'text']
    rows = results
    for row in rows:
        if row == None:
            rows.remove(row)
    with open(outfile_name, 'w', encoding='UTF-8', newline= '') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except TypeError:
                pass


main()
