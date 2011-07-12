print "Type only numbers!"
try:
    while True:
        input = raw_input("> ")
        if int(input) == 42:
            break
except ValueError:
    print "I said only numbers!"
