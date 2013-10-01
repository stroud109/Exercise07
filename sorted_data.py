from sys import argv

script, filename = argv 

filename = open("scores.txt") 

restaurant_data = filename.read()

print restaurant_data

#put data in dict first bc dict is unordered
#alphabetize the contents and assign to something ordered 

ratings_dict = {} 

for line in restaurant_data:
    