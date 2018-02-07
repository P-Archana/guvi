num=input("enter the no")
sum=0
l=len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** l
   temp /= 10
if num == sum:
   print str(num)+" is an Armstrong number"
else:
   print str(num)+" is not an Armstrong number"
