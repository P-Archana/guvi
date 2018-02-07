string1=raw_input("enter string")
str1=''
for i in range(0,len(string1),2):
    str1+=''.join(string1[i+1]+string1[i])
print str1