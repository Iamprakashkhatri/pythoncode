l1=[1,2]
l2=[4,5]
l3=[]
# output:[[1,4],[1,5],[2,4],[2,5]]
for item in l1:
    for item1 in l2:
        l3.append([item,item1])
print(l3)