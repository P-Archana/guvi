s=raw_input('enter roman numeral')
num = { 'X':10, 'V':5, 'I':1}
n = 0
l = 0
for value in (num[c] for c in reversed(s.upper())):
    v = (value, -value)[value < l]
    n += (value, -value)[value < l]
    l = value
print n