input = None
while True:
    try:
        input = raw_input("Gimme a number >")
        num = int(input)
    except ValueError:
        print "'%s' isn't a number, bro" % input
        continue

    print "%f seems like a good number, thanks yo" % num
    
