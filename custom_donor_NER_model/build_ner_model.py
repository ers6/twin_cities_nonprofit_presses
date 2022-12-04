import spacy
import csv
from spacy.tokens import DocBin
from tqdm import tqdm

def main():
    nlp = spacy.blank("en")
    the_results = csv_to_dict("/Users/elizabethschwartz/Documents/nonprofit press project/named_entity_experiments/data/training_entities.csv")
    list_training_ents = []
    donor_lists = []
    for result in the_results:
        list_training_ents.append(result['training_ents'].strip().split('||'))
        donor_lists.append(result['text'].replace(r'\n', ''))
    # print(list_training_ents)

    nlp.add_pipe('sentencizer')
    corpus = []
    for donor_list in donor_lists:
        doc = nlp(donor_list)
        for sent in doc.sents:
            corpus.append(sent.text)
    patterns = []
    for entry in list_training_ents:
        for item in entry:
            patterns.append({"label": "DONOR", "pattern": item.strip()})
    # print(patterns)
    # print(len(patterns))
    # Create the EntityRuler
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    TRAIN_DATA = []
    for sentence in corpus:
        doc = nlp(sentence)
        entities = []

        for ent in doc.ents:
            entities.append([ent.start_char, ent.end_char, ent.label_])
        TRAIN_DATA.append([sentence, {"entities": entities}])
    print(len(TRAIN_DATA))
    validating = TRAIN_DATA[345:690]
    testing = TRAIN_DATA[690:710]
    with open("testing_data.txt", "w") as outfile:
        print(testing, file=outfile)
    TRAIN_DATA = TRAIN_DATA[0:345]
    donor_train_data = convert(TRAIN_DATA)
    donor_train_data.to_disk("data/training.spacy")
    donor_valid_data = convert(validating)
    donor_valid_data.to_disk("data/validating.spacy")
    print('congrats! you have created the training data sets. they are stored in the data directory')
    print('next you need to download the baseconfig file from spacy and train the model in the command line.')
    print('download the base config file here: https://spacy.io/usage/training')
    print('or visit this github notebook for a tutorial: https://ner.pythonhumanities.com/03_02_train_spacy_ner_model.html')



def convert(TRAIN_DATA):
    nlp = spacy.blank("en")
    db = DocBin()
    for text, annot in tqdm(TRAIN_DATA):
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print('skipping entity')
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    return db




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

main()