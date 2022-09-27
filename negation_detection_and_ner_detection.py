import spacy
from spacy import displacy

med_ner = spacy.load("D:\\Final Year Project\\new_model\\model-best")
doc = med_ner("""Leafy vegetables, fruits, and mollusks were the most common sources of foodborne norovirus outbreaks from 2001 to 2008 according to analysis of data from the Foodborne Disease Outbreak Surveillance System of the Centers for Disease Control and Prevention. Infected food handlers were thought to be the source of contamination in at least half of reported norovirus outbreaks.

Data from 2,922 reported cases was analyzed by Aron J. Hall, DVM, MSPh, an epidemiologist with the CDC, and colleagues. The goal was to identify areas for potential intervention in the contamination process. The study results were presented most recently at the 7th Annual OutbreakNet Conference in Long Beach, CA in September 2011.

According to the researchers, there are approximately 5.5 million foodborne illnesses each year in the US attributed to norovirus, which is the leading cause of foodborne disease outbreaks. This virus has a fecal-oral transmission route and is known for its ability to spread rapidly and efficiently.

Data collected included outbreak and patient characteristics, place of food preparation, and probable food vehicle. All cases in which norovirus was confirmed or suspected as the cause of illness were included. Forty-nine states reported foodborne norovirus outbreaks, and there was considerable variation in reporting rates between states.

Eighty-three percent of norovirus outbreaks involved foods prepared in commercial settings, most commonly in restaurants or delicatessens. A food handler was identified as the contamination source in 53% of the outbreaks and as a potential source in as many as 82%, the researchers report.

A single food was implicated in 364 foodborne norovirus outbreaks. The most common food to be implicated was leafy vegetables at 33%, followed by fruits and nuts at 16%, and mollusks at 13%. All commodities except sprouts were implicated in at least one outbreak.

This study highlights the frequency of contamination of ready-to-eat and raw foods.

Recommendations from this study include “adherence to appropriate recommendations for hand washing and use of gloves; compliance with policies to prevent ill staff from working; and presence of a certified kitchen manager, as recommended by the Food Code of the US Food and Drug Administration.”

The authors report no financial conflicts of interest.""")



displacy.serve(doc, style="ent") 