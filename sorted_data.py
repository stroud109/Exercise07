'''
create dictionary
alphabetize restaurants
print alphabetized restaurants along with ratings
'''


from sys import argv
import collections

script, text_file_name = argv 

text_file = open(text_file_name) 
restaurant_data = text_file.readlines()
# readlines (plural) is different from readline (singular)

# print restaurant_data

ratings_dict = {} 

for line in restaurant_data:
	restaurant_name, restaurant_score = line.split(":")
	ratings_dict[restaurant_name] = int(restaurant_score.strip("\n "))
	# dictionary[key] = value
# print ratings_dict

# http://stackoverflow.com/questions/9001509/python-dictionary-sort-by-key
ordered_ratings_dict = collections.OrderedDict(sorted(ratings_dict.items()))
for restaurant_name, restaurant_score in ordered_ratings_dict.iteritems():
	# print restaurant_name, restaurant_score
	print "Restaurant '%s' is rated at %d." % (restaurant_name, restaurant_score)
