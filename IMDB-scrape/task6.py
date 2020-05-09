from task5 import *

movies_list=get_movie_list_detail()
for i in movies_list:
	print(i['language'])