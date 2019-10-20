list1 = ["a","b","c"]
# When you need only values in list
for item in list1:
    print(item)
# When you need only index from list
for index in range(len(list1)):
    print(index)
# When you need both index and item values
for index,item in enumerate(list1):
    print(index,item)