list1=[{'name':"Ram"},{'name':"Shyam"},{'name':"Ram"},{'name':"Hari"}]
list2=[]
for name in list1:
    for name1 in name.values():
        list2.append(name1)
print(set(list2))