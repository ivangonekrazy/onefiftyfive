u = "name"
p = "passwort"
l = True
c = 0

while l:
    username = raw_input("enter username >") 
    password = raw_input("enter password >") 
    if username == u and password == p:
        print "OKAY"
        print "User tried %r times" % (c)
        l = False
    else:
        print "FAIL \a"
        c = c + 1
    
print "Done."
