import json
from pprint import pprint

dict_of_genre={}

data=json.load(open("scrape4.json"))
for genre in data:
	for i in genre["genre"]:
		if i not in dict_of_genre:
			dict_of_genre[i]=1
		else:
			dict_of_genre[i]+=1
with open("scrape11.json","w") as scrape_genre:
	json.dump(dict_of_genre,scrape_genre,indent=4)
