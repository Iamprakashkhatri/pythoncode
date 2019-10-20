num=int(input("A no:"))
sum=0
temp=num
length=len(str(num))
while(temp!=0):
    sum=sum+(temp%10)**length
    temp=temp//10
if sum==num:
    print("armstrong no.")