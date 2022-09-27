
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

nlp = spacy.blank("en") #load new spacy model
db = DocBin() #create a DocBin Object

import json
f = open("annotations(1).json",encoding="utf8")
f1 = open("annotations(2).json",encoding="utf8")
TRAIN_DATA = json.load(f) #loaded the annotations
TRAIN_DATA_1 = json.load(f1)


def add_to_doc(dataset):
	for text , annot in tqdm(dataset['annotations']):
		doc = nlp.make_doc(text)
		ents = []
		for start , end , label in annot["entities"]:
			print("start: ",start)
			print("end:", end)
			print("label:" , label)
			span = doc.char_span(start , end , label= label, alignment_mode = "contract")
			print("span: ",span)

			if span is None:
				print("Skipping Entity")
			else:
				ents.append(span)
		doc.ents = ents 
		db.add(doc)

add_to_doc(TRAIN_DATA)
add_to_doc(TRAIN_DATA_1)




db.to_disk("./med_training_data.spacy") # save the docbin object

#spacy config widget
""" English
	ner
	CPU
	accuracy
"""
# python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy
# python -m spacy train config.cfg --output ./new_model --paths.train ./med_training_data.spacy --paths.dev ./med_testing_data.spacy
