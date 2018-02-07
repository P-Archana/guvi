a=[]
n=int(input("enter the limit"))
for i in range(1,n+1):
    b=int(input("enter the element"))
    a.append(b)
k=int(input("enter the no of elements to be added"))
sum=0
for i in range(0,k):
    sum=sum+a[i]
print sum