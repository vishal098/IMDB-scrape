import requests,os,json,pprint
from bs4 import BeautifulSoup

def scrap_top_list():
	if os.path.exists("scrape.json"):
		print("file hai or data yaha se le raha he")
		with open("scrape.json","r") as file:
			top_list = json.load(file)
			return top_list
	else:
		print("file nahi hai to req me time lag raha hai")
		url=('https://www.imdb.com/india/top-rated-indian-movies/')
		response = requests.get(url)
		data = BeautifulSoup(response.text,('html.parser'))
		main_div=data.find('div',class_='lister')
		tbody=main_div.find('tbody',class_='lister-list')
		trs=tbody.find_all('tr')
		movie_name=[]
		movie_rank=[]
=		year_of_realease=[]
		movie_url=[]
		movie_ratings=[]
		for tr in trs:
			position = tr.find('td',class_='titleColumn').get_text().strip()
			rank=''
			for i in position:
				if '.' not in i:
					rank+=i
				else:
					break
			movie_rank.append(rank)
			title=tr.find('td',class_='titleColumn').a
			movie_name.append(title.get_text())

			year=tr.find('td',class_='titleColumn').span.get_text().strip('()')
			year_of_realease.append(year)

			m_link=tr.find('td',class_='titleColumn').a['href']
			movie_url.append('https://www.imdb.com'+m_link)

			rating=tr.find('td',class_='ratingColumn imdbRating').strong
			movie_ratings.append(rating.get_text())
		top_list=[]
		empty={'name':'','year':'','position':'','rating':'','url':''}
		for i in range(len(movie_rank)):
			empty['name']=str(movie_name[i])
			# year_of_realease= year_of_realease[i]
			empty['year']=int(year_of_realease[i])
			empty['position']=int(movie_rank[i])
			empty['rating']=float(movie_ratings[i])
			empty['url']=str(movie_url[i])
			top_list.append(empty.copy())
		with open("scrape.json","w") as file:
			json.dump(top_list,file)
			return top_list
if __name__=='__main__':
	top_movies = scrap_top_list()
	pprint.pprint(top_movies)
