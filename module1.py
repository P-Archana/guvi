import datetime
import random
print("1.login")
print("2.create account")
print("enter option")
str1=int(raw_input())
if str1==2:
    print("enter username")
    user1=raw_input("username")
    print("enter password")
    pass1=raw_input("password")
    print("acc. created\n\n login again")
    str1=1
if str1==1:
    print("enter username")
    user=raw_input("username")
    print("enter password")
    pas=raw_input("password")
if pas==pass1 and user==user1:
    print("enter station name from the list\n madurai\n trichy\n chennai")
    fromS=raw_input("From Station")
    Tos=raw_input("To Station")
    DateJor =raw_input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, DateJor.split('-'))
    dict1={'chennai':'0','trichy':'1','madurai':'2'}
    dict2 ={'chennai':'0','trichy':'1','madurai':'2'}
    trainlist={'01':'rockfort express','02':'pallavan express','10':'pandyan express','12':'vaigai express','20':'mangalore express','21':'madurai express'}
    trainlist1={'01':'shatabdi express','02':'sethu express','10':'rameswaram express','12':'podigai express','20':'maq express','21':'sengottai express'}
    w=dict1[fromS]+dict2[Tos]
    print '1.', trainlist[w],'2.', trainlist1[w]
    num=input("enter option")
    if num==1:
        trainname=trainlist[w]
    else:
        trainname=trainlist[w]
    trainno=int(w)
seat_ac1=80
seat_ac2=80
seat_ac3=80
seat_sleeper=80
print "\t\t\t  ENTER THE  DETAILS"
if(seat_ac1>0):
    no_ofac1stclass=int(raw_input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED : "))
if(seat_ac2>0):
    no_ofac2ndclass=int(raw_input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED : "))
if(seat_ac3>0):
    no_ofac3rdclass=int(raw_input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED : "))
if(seat_sleeper>0):
    no_ofsleeper=int(raw_input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED : "))
nameall=[]
ageall=[]
genderall=[]
berthall=[]
for i in range(0,no_ofac1stclass):
	name=raw_input("enter the passenger name in ac1stclass : ")
	age=raw_input("enter the age : ")
	gender=raw_input("enter the gender : ")
	berth_array=['lower','upper','middle']
	b=random.randint(0,2)
	berth=berth_array[b]
	if age>'50':
		berth='lower'
	seat_ac1=seat_ac1-1
nameall.append(name)
ageall.append(age)
genderall.append(gender)
berthall.append(berth)
for i in range(0,no_ofac2ndclass):
	name=raw_input("enter the passenger name in ac2ndclass: ")
	age=raw_input("enter the age : ")
	gender=raw_input("enter the gender : ")
	berth_array=['lower','upper','middle']
	b=random.randint(0,2)
	berth=berth_array[b]
	if age>'50':
		berth='lower'
	seat_ac2=seat_ac2-1
nameall.append(name)
ageall.append(age)
genderall.append(gender)
berthall.append(berth)
for j in range(0,no_ofac3rdclass):
    name=raw_input("enter the passenger name in ac3rdclass: ")
    age=raw_input("enter the age : ")
    gender=raw_input("enter the gender : ")
    berth_array=['lower','upper','middle']
    b=random.randint(0,2)
    berth=berth_array[b]
    if age>'50':
        berth='lower'
    seat_ac3=seat_ac3-1
nameall.append(name)
ageall.append(age)
genderall.append(gender)
berthall.append(berth)
for i in range(0,no_ofsleeper):
	name=raw_input("enter the passenger name in sleeper: ")
	age=raw_input("enter the age : ")
	gender=raw_input("enter the gender : ")
	berth_array=['lower','upper','middle']
	b=random.randint(0,2)
	berth=berth_array[b]
	if age>'50':
		berth='lower'
	seat_sleeper=seat_sleeper-1
nameall.append(name)
ageall.append(age)
genderall.append(gender)
berthall.append(berth)
total=no_ofac1stclass+no_ofac2ndclass+no_ofac3rdclass+no_ofsleeper
print "\n\n===================TICKET=================\n\n"
print "THE ENTERED TRAIN NAME IS : ",trainname
print "THE TRAIN  NUMBER IS : ",trainno
print "STARTING POINT ENTERED IS : ",fromS
print "DESTINATION POINT ENTERED IS : ",Tos
print "NO_OF AC FIRST CLASS SEATS  :",no_ofac1stclass
print "NO_OF AC SECOND CLASS SEATS :",no_ofac2ndclass
print "NO_OF AC THIRD CLASS SEATS :",no_ofac3rdclass
print "NO_OF SLEEPER CLASS SEATS :",no_ofsleeper
for i in range(0,total):
    print "passenger name :", nameall[i]
    print "age :",ageall[i]
    print "gender :",genderall[i]
    print " berth :",berthall[i]