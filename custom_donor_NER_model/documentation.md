# About the NER model

I created a custom NER model to pull donor names out of donor lists. To do so, I annotated 96/960 (10% of the total corpus) of the donor lists successfully scraped from the books. I chose these 96 titles randomly. 

Following the creation of training data, I set up a simple named entity recognition model using spaCy. spaCy is an open source natural language processing python library. It offers many large language models across multiple different languages. I used the small English model to build my NER model on top of. 

## On LLMs & Empire: A Brief Interlude

spaCy, along with any other large language model (LLM),  is complicit in climate change and other forms of colonial, racialized violence. As Lauren Klein explains in her August 2022 article, the creation of LLMs (necessary for NLP research) is dependent on computational analysis of massive data sets. This requires access to super computers and computing power that rarely exists outside of military contexts. The implications of LLM's development is inseparable from the military industrial complex. Moreover, the amount of energy consumed in the training of LLM has a major impact on climate change. 

The LLM upon which spaCy is built no exception. Developers trained spaCy's English, Chinese, and Arabic models on the OntoNotes dataset, created by the US Department of Defense in collaboration with researchers at the University of Pennsylvania, the University of Southern California, the University of Colorado Boulder, and Brandeis University. I don't know enough about OntoNotes to say what exactly the DOD intended to do with it. However, in its documentation, the researchers provide rather telling examples of how the program might be used: 

"consider this sentence: 'The founder of Pakistan's nuclear program, Abdul Qadeer Khan, has admitted that he transferred nuclear technology to Iran, Libya, and North Korea.'"

The researchers go on to show how models trained on the OntoNotes corpus can parse the sentence to trace the transmission of nuclear technology across the global South. 

  I was hesitant to use spaCy due to its complicity in US imperialism. Unfortunately, pretty much any computational tool at my disposal was/is developed by the DOD (including the internet). But beyond my moral objections to the OntoNotes project, I was concerned that the DOD might consume the data created in this project to further refine their dataset and models. However, I don't think my dataset is big enough and my model is simply not good enough to be of any use to the DOD. Furthermore, most of my data is located exclusively on my computer, not the internet (although you probably could duplicate my process and gather my same data set following the steps outlined in this github repo).
  Ultimately I came to the decision to use spaCy in spite of its complicity in climate disaster and imperialism. This project is therefore complicit in the naturalization of nlp technology in the digital humanities. I hope through walking through my own considerations of the inequities and harms nlp perpetuates, I can encourage other scholars to think critical about this technology. Think about alternatives. Ask yourself, how big is this dataset and to whom--beyond my intended audience--could it be useful? Finally, consider giving some things up. In liue of a more accurate model, perhaps use a less powerful, but less energy-consumptive alternative. 


Klein, Lauren. “Are Large Language Models Our Limit Case?” _Startwords_, no. 3 (August 1, 2022). [https://doi.org/10.5281/zenodo.6567985](https://doi.org/10.5281/zenodo.6567985).


