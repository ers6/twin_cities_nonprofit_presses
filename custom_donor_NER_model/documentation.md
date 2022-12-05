# About the NER model

I created a custom NER model to pull donor names out of donor lists. To do so, I annotated 96/960 (10% of the total corpus) of the donor lists successfully scraped from the books. I chose these 96 titles randomly. 

Following the creation of training data, I set up a simple named entity recognition model using spaCy. spaCy is an open source natural language processing python library. It offers a many large language models across multiple different languages. I used the small English model to build my NER model on top of. 

As Lauren Klein has argued, no large language model can escape complicity in climate change and other forms of violence. This is because to develop large language models (necessary for NLP research), developers need to analyze massive data sets. This requires access to super computers and computing power that rarely exists outside of military contexts. spaCy is no exception.  spaCy's English, Chinese, and Arabic models run on a neural net, OntoNotes, created by the US Department of Defense in collaboration with researchers at the University of Pennsylvania, the University of Southern California, the University of Colorado Boulder, and Brandeis University. I don't know enough about OntoNotes to say what exactly the DOD intended to do with it. However, in its documentation, the researchers provide rather telling examples of how the program might be used: 

"consider this sentence: 'The founder of Pakistan's nuclear program, Abdul Qadeer Khan, has admitted that he transferred nuclear technology to Iran, Libya, and North Korea.'"

The researcher go on to show how models trained on the OntoNotes corpus can parse the sentence to trace the transmission of nuclear technology across the global South. 

  I was hesitant to use spaCy due to its complicity in US imperialism. Unfortunately, pretty much any computational tool at my disposal was/is developed by the DOD (like, ya know, the internet). But beyond my distaste for the OntoNotes project, I was concerned that the DOD might consume the data


Klein, Lauren. “Are Large Language Models Our Limit Case?” _Startwords_, no. 3 (August 1, 2022). [https://doi.org/10.5281/zenodo.6567985](https://doi.org/10.5281/zenodo.6567985).


