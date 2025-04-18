
import requests
import csv
import os


# base API URL

url = "https://rickandmortyapi.com/api/character"

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

# #print the flitered list
# for char in new_character_list:
#      print(char['name'])

#create csv file

character_csv = open('character.csv','w')
character_csv.writelines('Id,Name,Status,Species, Origin Location Name, Last Known Location Name\n')
#paginate by using extracting the url found under 'info' in the api response- loop while URL is TRUE/not = to NONE
while url:
    try:
        response = requests.get(url)
        data = response.json()
     #simplify the original data list into fewer key/value pairs with 'map'
     #apply the function simplify to every item in the list data['results']
        new_character_list = map(simplify, data['results'])
     
        url = data['info']['next']
    #  print(url)
    #  for row in new_character_list:
    #     print(row)
# print("last",url)  
     
        for row in new_character_list:
            character_csv.writelines(str(row["id"]) +"," + row['name']+"," +row['status']+"," +row['species'] + ","+row['origin.name'] +","+ row['location.name']+"\n")
          
    except requests.exceptions.RequestException as e:
        print("Error Occured: ", e)
        
character_csv.close()

csv_filename = 'character.csv'

# check if file was created or not
if os.path.exists(csv_filename):
    print("character.csv was written successfully!")
    print(f"Find the file here: {os.path.abspath(csv_filename)}")
else:
    print("character.csv was not created.")






