str1=raw_input("enter string1")
str1=str1.upper()
dict={"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THURSDAY":4,"FRIDAY":5,"SATURDAY":6,"SUNDAY":7}
if dict[str1]==6 or dict[str1]==7:
    print 'Holiday'
else:
    print 'No Holiday'