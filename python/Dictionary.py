movie_info={"moviename":"Kingdom","budget":"70cr","releasedate":"31/7/2025"}
print(movie_info)

# i want to genre-action
movie_info['genre']='action'
print(movie_info)

movie_info['cast']=['VD','SD','BHAGYASRI']
print(movie_info)

movie_info["remuneration"]={'VD_rem':'25cr','SD_rem':'5cr','Bhagyasri':'2cr'}
print(movie_info)

#VD is charging 25cr for acting  in kingdom movie

print(f"{movie_info['cast'][0]} is charging {movie_info['remuneration']['VD_rem']} for acting {movie_info['moviename']} movie " )

#deleting property from dictionary
del movie_info['genre']
print(movie_info)


movie_name=['Kingdom','HHMV','Coolie','War2']
print(movie_name)
print(movie_name[len(movie_name)-1]) #to access last element from the list

#want to add value/element at the last index of the list

op=movie_name+['M.S.DHONI']
print(op)


kiran=frozenset()
print(kiran)