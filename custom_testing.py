import json
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

nlp = spacy.blank("en") #load new spacy model
db = DocBin() #create a DocBin Object


f = open("annotations(3).json",encoding="utf8")
TRAIN_DATA = json.load(f) #loaded the annotations

for text , annot in tqdm(TRAIN_DATA['annotations']):
	doc = nlp.make_doc(text)
	ents = []
	for start , end , label in annot["entities"]:
		span = doc.char_span(start , end , label= label, alignment_mode = "contract")
		if span is None:
			print("Skipping Entity")
		else:
			ents.append(span)
	doc.ents = ents 
	db.add(doc)


db.to_disk("./med_testing_data.spacy") # save the docbin object
