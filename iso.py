def iso(string1, string2):
    s1 = len(string1)
    s2 = len(string2)
    if s1 != s2:
        print 'no'
    marked = [False]*256
    map = [-1] *256
    for i in xrange(s1):
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                print 'no'
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            print 'no'
        else:
            print 'yes'
iso('aab','xxy')