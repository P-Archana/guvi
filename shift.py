a=int(raw_input("enter array size"))
k=int(raw_input("enter shift size"))
arr=list()
for i in range(0,a):
    n=input()
    arr.append(n)
for i in range(0,a):
    print arr[i-k]
