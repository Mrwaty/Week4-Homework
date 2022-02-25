import requests
import random

my_list=[]
len_list=[]
for i in range(10):
    
    r=requests.get("https://randomuser.me/api/")
    name=r.json()["results"][0]["name"]["first"]
    surname=r.json()["results"][0]["name"]["last"]
    city=r.json()["results"][0]["location"]["city"]
    country=r.json()["results"][0]["location"]["country"]

    x="".join((name+surname+city+country).split()).lower()

    x_shuffle=''.join(random.sample(x,len(x)))
    my_list.append(x_shuffle)

    len_list.append(len(my_list[i]))
    
print(my_list)
print("Lengths of characters in the list: " , len_list)

for j in range(10):  
    if max(len_list)== len_list[j]:
        print("'" , my_list[j] , "'", " has the most characters!")

"""
General Information:
I want to choose random information with the requests module.

Acceptance Criteria
* Get the name, surname, city and country information of a random person by using the requests module.
(Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
* Make lowercase and adjacent by removing the spaces.
(Example=> ambermurraysalisburyunitedkingdom)
* Then randomly shuffle the location of all the characters.
(Example=> mberarrumasyarubsiluniydetmdoingk)
* Apply this process for 100 different people and write in a list.
* Find that has the most characters and print it.

"""
