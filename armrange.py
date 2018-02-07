num1=input("enter the lower no")
num2=input("enter the upper no")

for num in range(num1,num2):
    temp = num
    sum=0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp /= 10
    if num == sum:
        print (num)
