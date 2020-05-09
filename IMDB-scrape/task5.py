from task1 import *
from task4 import *

def get_movie_list_detail():
	if  os.path.exists("scrape4.json")==False:
		movies_=scrap_top_list()[:10]
		movies_data=[]
		for i in movies_:
			# print(i['url'])
			k=movie_details(i['url'])
			# pprint.pprint(k)	
			movies_data.append(k)
		with open("scrape4.json","w") as file:
			json.dump(movies_data,file)
			open('scrape4.json','w').close()
		# pprint.pprint(movies_data)

	print("file hai or data yaha se le raha he")
	with open("scrape4.json","r") as file:
		demo_details = json.load(file)
	return(demo_details)


if __name__=='__main__':
	pprint.pprint(get_movie_list_detail())



