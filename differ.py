str1=raw_input("enter string1")
str2=raw_input("enter string2")
count=0
if len(str1)!= len(str2):
    print 'the strings are not of same length'
else:
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count+=1
    print count