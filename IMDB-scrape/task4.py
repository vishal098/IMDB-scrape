import requests,os,json,pprint
from bs4 import BeautifulSoup

# def movie_details():
# 	url=('https://www.imdb.com/title/tt6148156/')
# 	r=requests.get(url)
# 	b=BeautifulSoup(r.text,'html.parser')
# 	demo_details={'name':'','director':[],'Country':'','Language':[],'poster_img_url':'','bio':'','runtime':'','genre':[]}
# 	name=b.find('div',class_='title_wrapper').h1.get_text()
# 	movie_name=''
# 	for i in name:
# 		if '(' not in i:
# 			movie_name=(movie_name+i).strip()
# 		else:
# 			break
# 	demo_details['name']=movie_name

# 	sub_div=b.find('div',class_='subtext')
# 	runtime=sub_div.find('time').get_text().strip()
# 	hour=int(runtime[0])*60
# 	if 'min' in runtime:
# 		minute=runtime.strip('min')
# 		minute=int(minute[3:])
# 		runtime=hour+minute
# 		demo_details['runtime']=runtime

# 	img_url=b.find('div',class_='poster').img['src']
# 	demo_details['poster_img_url']=img_url

# 	genre1=sub_div.find_all('a',title="")
# 	for i in genre1:
# 		print(i.get_text())
# 	demo_details['genre']=genre

# 	plot=b.find('div',class_='plot_summary_wrapper')
# 	# bio=plot.find('div',class_='summary_text').text
# 	# demo_details['bio']=bio

# 	director1=b.find_all('div',class_='credit_summary_item')
# 	for i in director1:
# 		tag_h4=i.find('h4')
# 		if 'Directors:' in tag_h4 or 'Director:' in tag_h4 :
# 			director=i.find_all('a')
# 			for j in director:
# 				# print(j.get_text())
# 			demo_details['director'].append(director)


# 	details=b.find('div',id="titleDetails")
# 	a=details.findAll('div',class_="txt-block")
# 	for i in a:
# 		tag_h4=i.find_all('h4')
# 		for j in tag_h4:
# 			if 'Country:' in j:
# 				Country=i.find('a').get_text()
# 				demo_details['Country']=Country
# 				# print(Country)
	
# 			if 'Language:' in j:
# 				Language=i.find_all('a')
# 				for l in Language:
# 					# print(l.get_text())
# 				demo_details['Language'].append(l.get_text())
# 	pprint.pprint(demo_details)
# movie_details()


def movie_details():

	print("file nahi hai to req me time lag raha hai")
	url=('https://www.imdb.com/title/tt6148156/')
	r=requests.get(url)
	b=BeautifulSoup(r.text,'html.parser')
	demo_details={'Name':'','director':[],'country':'','language':[],'poster_img_url':'','bio':'','runtime':'','genre':[]}
	name=b.find('div',class_='title_wrapper').h1.text
	movie_name=''
	for i in name:
		if '(' not in i:
			movie_name=(movie_name+i).strip()
		else:
			break
	demo_details['Name']=movie_name

	sub_div=b.find('div',class_='subtext')
	runtime=sub_div.find('time').text.strip()
	hour=int(runtime[0])*60
	if 'min' in runtime:
		minute=runtime.strip('min')
		minute=int(minute[3:])
		runtime=hour+minute
		demo_details['runtime']=runtime

	img_url=b.find('div',class_='poster').img['src']
	demo_details['poster_img_url']=img_url

	genre1=sub_div.find_all('a',title="")
	for i in genre1:
		# print(i.get_text())
		demo_details['genre'].append(i.get_text())

	bio=b.find('div',class_='summary_text').get_text().strip()
	# print(bio)
	demo_details['bio']=bio

	director1=b.find_all('div',class_='credit_summary_item')
	for i in director1:
		tag_h4=i.find('h4')
		if 'Directors:' in tag_h4 or 'Director:' in tag_h4 :
			director=i.find_all('a')
			for j in director:
				# print(j.get_text())
				demo_details['director'].append(j.get_text())

	details=b.find('div',id="titleDetails")
	a=details.findAll('div',class_="txt-block")
	for i in a:
		tag_h4=i.find_all('h4')
		for j in tag_h4:
			if 'Country:' in j:
				Country=i.find('a').text
				demo_details['country']=Country
				# print(Country)
	
			if 'Language:' in j:
				Language=i.find_all('a')
				for l in Language:
				# print(l.get_text())
					demo_details['language'].append(l.get_text())
	return demo_details
if __name__=='__main__':
	pprint.pprint(movie_details())
		
	


