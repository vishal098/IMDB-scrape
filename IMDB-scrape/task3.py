from task2 import *

def group_by_decade(movies):
	movie_dec={}
	lst=[]
	for index in movies:
		# print(index)
		dec=index%10
		mod=index-dec
		if mod not in lst:
			lst.append(mod)
	lst.sort()
	for i in lst:
		movie_dec[i]=[]
		# print(movie_dec)
	for i in movie_dec:
		# print(i,'\n')
		x=i+9
		for check in movies:
			# print(check)
			if i <= check <= x:
				# print(i,'\n',check,'\n')
				for z in movies[check]:
					# print(z)
					movie_dec[i].append(z)
	return (movie_dec)
name_sort=group_by_decade(dec_arg)

if __name__=='__main__':
	pprint.pprint(name_sort)