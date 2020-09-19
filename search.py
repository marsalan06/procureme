from googlesearch import search 
  
# to search 
l=["BuyAliexpress", "BuyAliBaba", "Buydaraz"]
for i in l:
    query = "MechanicalThreadNut" + i
    for j in search(query, tld="com", num=5, stop=5, pause=2): 
        print(j,type(j)) 