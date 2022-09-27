from __future__ import unicode_literals, print_function
import random
from pathlib import Path
from spacy.util import minibatch , compounding
import spacy
import sys
from Corona2_TRAIN_DATA import TRAIN_DATA
from spacy.training import Example

spacy.util.use_gpu(0)
def train_model(model = None , output_dir = "/NER Output/", n_iter = 1000):
	if model is not None:
		nlp = spacy.load(model)	
		print("Model loaded : ", model)
	else:
		nlp = spacy.blank("en")	
		print("Create blank model")
	
	if "ner" not in nlp.pipe_names:
		# ner = nlp.create_pipe("ner")
		ner = nlp.add_pipe("ner", last=True)
	else:
		ner = nlp.get_pipe("entity_ruler")
	for _, annotations in TRAIN_DATA:
		for ent in annotations.get("entities"):
			ner.add_label(ent[2])

	pipe_exceptions = ["ner" , "trf_wordpiecer","trf_tok2vec"]
	other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
	with nlp.disable_pipes(*other_pipes): #only training NER
		if model is None:
			nlp.begin_training()
		for itn in range(n_iter):
			losses = {}
			# examples = []
			# for texts, annots in TRAIN_DATA:
			# 	examples.append(Example.from_dict(nlp.make_doc(text),annots))
			# nlp.initialize(lambda: examples)

			# for i in range(20):
			# 	random.shuffle(examples)
			# 	for batch in minibatch(examples , size = 20)
			# 		nlp.update(batch, drop = 0.20 , losses = losses)
			
			# random.shuffle(TRAIN_DATA)
		
			# batches = minibatch(TRAIN_DATA , size = compounding(4.0 , 64.0 , 1.2))
			# for batch in batches:
			# 	texts, annotations = zip(*batch)
			# 	nlp.update(
			# 		texts,
			# 		annotations,
			# 		drop = 0.20,
			# 		losses = losses
			# 	)
			examples = []
			for text, annots in TRAIN_DATA:
			 #    span = doc.char_span(start_char, end_char, label=label, alignment_mode="expand")
				# adjusted_start_char = span.start_char
				# adjusted_end_char = span.end_char
				
			    examples.append(Example.from_dict(nlp.make_doc(text), annots))

			nlp.initialize(lambda: examples)
			for i in range(20):
			    random.shuffle(examples)
			    for batch in minibatch(examples, size=8):
			        nlp.update(batch , drop = 0.20 , losses = losses)
			print("Losses",losses)
	
	#saving model to output directory
	if output_dir is not None:
		output_dir = Path(output_dir)
		if not output_dir.exists():
			output_dir.mkdir()
		nlp.to_disk(output_dir)
		print("Saved model to", output_dir)
 
train_model()
