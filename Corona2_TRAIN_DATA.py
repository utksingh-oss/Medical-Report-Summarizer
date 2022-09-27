import json
with open("Corona2.json") as f:
	annotations = json.load(f)

TRAIN_DATA = []
for expl in annotations["examples"]:
	content = expl["content"]
	entities = []
	for anno in expl["annotations"]:
		if len(anno["value"]) == len(anno["value"].strip()):
			if(len(anno["human_annotations"])) == 0: 
				continue
			info = (anno["start"],anno["end"],anno["tag_name"])
			entities.append(info)
		if(len(entities)) > 0:
			TRAIN_DATA.append(([content , {"entities":entities}]))