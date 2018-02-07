num=int(input("Enter no.:"))
fact=1
if num==1:
    print ' factorial value is 1'
else:
    for i in range(1,num+1):
        fact=fact*i
    print fact
