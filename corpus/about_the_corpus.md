# About the corpus

The corpus contains 1137 volumes published by 4 501c3 nonprofit book publishers in the twin cities of Minneapolis and St. Paul: Graywolf Press, Milkweed Editions, Coffee House Press, and New Rivers. View the collection and download the json metadata records at HathiTrust: [https://babel.hathitrust.org/cgi/mb?a=listis&c=1276895566](https://babel.hathitrust.org/cgi/mb?a=listis&c=1276895566)


# What's in this directory?

 - **analyze_corpus.py** is a python program that supplements the hathitrust metadata records with: 
	 - the address of the press at the time of publication as a string, 
	 - the 501c3 status of the press as a boolean (True = 501c3, False = not 501c3), 
	 - and whether or not the press was in the Twin Cities at the time of publication as a boolean (True = in Twin Cities, false= not in Twin Cities)
- **supplemented_collection_metadata.json** is the json file **analyze_corpus.py** creates with the added metadata fields. 
