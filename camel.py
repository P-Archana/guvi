string1=raw_input("enter string")
str1=''
for i in range(0,len(string1)):
    if i==0 or string1[i-1]==' ':
        str1+=''.join(string1[i].upper())
    else:
        str1+=''.join(string1[i])
print str1