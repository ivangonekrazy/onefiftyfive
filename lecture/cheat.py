region = raw_input('North or South? > ')
school = raw_input('School name > ')

region = region.lower()
school = school.lower()

if region == 'north':
    if school == "uc berkeley":
        print "Go Bears!"
    elif school == "stanford":
        print "Go Cardinals!"
elif region == "south":
    if school == "ucla":
        print "Go Bruins!"
    elif school == "usc":
        print "Go Trojans!"
print 'done.'
