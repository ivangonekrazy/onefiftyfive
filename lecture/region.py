region = raw_input('North or South? > ')
school = raw_input('School name > ')

if region == 'North':
    if school == "UC Berkeley":
        print "Go Bears!"
    elif school == "Stanford":
        print "Go Cardinals!"
elif region == "South":
    if school == "UCLA":
        print "Go Bruins!"
    elif school == "USC":
        print "Go Trojans!"

