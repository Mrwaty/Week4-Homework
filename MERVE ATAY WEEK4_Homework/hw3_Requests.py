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