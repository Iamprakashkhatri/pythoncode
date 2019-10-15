l1=[1,2,3]
l2=['a','b','c']
l3=[]
for index,item in enumerate(l1):
    l3.append([item,l2[index]])
print(l3)