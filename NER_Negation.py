import spacy
import stanza
import datetime
from adding_patients_diag import PatientDiagHelper

import spacy_stanza
from negspacy.negation import Negex
from negspacy.termsets import termset
import pandas as pd

nlp = spacy_stanza.load_pipeline('en', package='mimic', processors={'ner': 'i2b2'})

ts = termset("en_clinical")
ts.add_patterns({
	'preceding_negations': ['abstain from' , 'other than' , 'except for' , 'except' , 'with the exception of' , 'excluding' , 'lack of' , 'contradication', 'contraindicated','interfere with', 'prohibit','prohibits'],
	'following_negations': ['negative','is allowed','impossible','exlusionary']
})

nlp.add_pipe("negex", config={"ent_types":["PROBLEM","TEST",'TREATMENT']})

class Get_Info:
	def __init__(self):
		print("Get Info Object Called")

	def get_data(patient_id , self):
		patient_helper = PatientDiagHelper()
		res = patient_helper.get_patients_diag(patient_id)


		for cur in res:
			diag = cur[3]
			problems_date = {}
			problems_count = {}
			tests_date = {}
			tests_count = {}
			treatments_date = {}
			treatments_count = {}

			doc_1 = nlp(diag)

			for e in doc_1.ents : 
			  if e.label_ == "TREATMENT" and e._.negex == False:
			    treatments_date[e.text] = datetime.datetime(2020 , 5, 17)
			    if e.text in treatments_count.keys():
			      treatments_count[e.text] += 1
			    else:
			      treatments_count[e.text] = 1
			  if e.label_ == "TEST" and e._.negex == False:
			    tests_date.date[e.text] = datetime.datetime(2020 , 5, 17)
			    if e.text in tests_count.keys() : 
			      tests_count[e.text] += 1
			    else:
			      tests_count[e.text] = 1
			  if e.label_ == "PROBLEM": 
			    problems_date[e.text] = datetime.datetime(2020 , 5 , 17)
			    if e.text in problems_count.keys(): 
			      problems_count[e.text] += 1
			    else : 
			      problems_count[e.text] = 1
		return [cur[2] , problems_date , tests_date , treatments_date]