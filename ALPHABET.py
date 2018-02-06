import string
n=raw_input('enter the value')
alphabet=string.ascii_lowercase+string.ascii_uppercase
if n in alphabet:
    print 'alphabet'
else:
    print 'not alphabet'