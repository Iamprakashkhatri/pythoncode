thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["model"] #Accessing item of dictionary
thisdict.get("model") #Accessing item using get method
thisdict["year"] = 2018 #Changing Values of Specific item by its key name
thisdict["color"] = "red" #Adding item to dictionary
thisdict.pop("model") #Removing item from dictionary using key name
thisdict.keys() #get all keys in dictionary
print(thisdict.keys())
thisdict.items() #get all items in dictionary
print(thisdict.items())
print(thisdict.values()) #get all values of keys in dictionary