from task1 import *

def group_by_year(movies):
	years=[]
	for i in movies:
		year=i['year']
		if year not in years:
			years.append(year)
	movie_dict={}
	for j in years:
		a=[]
		for i in movies:
			if j==(i['year']):
				a.append(i)
				movie_dict[j]=a
	return(movie_dict)
scrapped=scrap_top_list()
dec_arg=( group_by_year(scrapped))

if __name__=='__main__':
	pprint.pprint(dec_arg)