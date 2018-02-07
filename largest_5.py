a=[]
n=3
for i in range(1,n+1):
    b=int(input("enter the element") )
    a.append(b)
a.sort()
print "largest no is",a[n-1]