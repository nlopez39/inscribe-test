
import requests
import csv


# fetch from API URL 

url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)
data = response.json()
# print(response.json())

#function that will reduce data to these few properties -> id, name, status, species, origin.name, and location.name
#char = characters in this function
def simplify(char):
    return{
        'id':char['id'],
        'name':char['name'],
        'status':char['status'],
        'species':char['species'],
        'origin.name':char['origin']['name'],
        'location.name':char['location']['name']

    }
#simplify the original data list into fewer key/value pairs with 'map'
# apply the function simplify to every item in the list data['results']
new_character_list = map(simplify, data['results'])
# #print the flitered list
# for char in new_character_list:
#     print(char)

#create csv file
with open('character.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'status', 'species', 'origin.name', 'location.name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in new_character_list:
        writer.writerow(row)




