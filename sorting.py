def hasArray(A,n):
    for item in A:
        for item1 in A:
            if (item+item1==n):
                return True

A = [1, 4, 45, 6, 10, -8] 
n = 16
if (hasArray(A,n)): 
    print("Array has two elements with the given sum") 
else: 
    print("Array doesn't have two elements with the given sum")