
import json
from pprint import pprint
file=json.load(open("scrape4.json","r+"))

directors={}

for dic in file:
	for j in dic["Director"]:	 
		if j not in directors:
			directors[j]={}

for k in directors:
	for d in file:
		for s in d["Director"]:
			if k==s:
				for lan in d["language"]:
					if lan not in directors[k]:
						directors[k][lan]=1
					else:
						directors[k][lan]+=1

with open("scrape10.json","w") as scrapedata:
	json.dump(directors,scrapedata,indent=4)