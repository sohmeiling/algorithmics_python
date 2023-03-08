##### ------------------------------------------------------------- #####
# 1 - Create Dictionary
print("########################################")
thisdict = dict()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": "$6000"
}

print(thisdict.keys()) #print the list of generaterd keys
print(thisdict.values()) #print the list of generated values
print(thisdict) # print the whole dictionary


##### ------------------------------------------------------------- #####
# 2 - Add items to dictionary
## Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict["color"] = "red"
print(thisdict)

thisdict["capacity"] = "1500cc"
print(thisdict)



##### ------------------------------------------------------------- #####
# 3 - Remove items from the dictionary
## The pop() method removes the item with the specified key name:
## The del keyword removes the item with the specified key name:
## The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.pop("model")
print(thisdict)

del thisdict["price"]
print(thisdict)

thisdict.popitem()
print(thisdict)



##### ------------------------------------------------------------- #####
# 4 - Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(thisdict["brand"])



##### ------------------------------------------------------------- #####
# 5 - Dictionaries cannot have two items with the same key
thisdict["year"] = 2023
print(thisdict)



##### ------------------------------------------------------------- #####
# 6 - Dictionary Length
print(len(thisdict))