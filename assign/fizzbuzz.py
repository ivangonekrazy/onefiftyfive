def fizzbuzz():
    """
        For each number in the range (1,100),
        print 'Fizz' if the number if a multiple of 3
        print 'Buzz' if the number if a multiple of 5
        print 'FizzBuzz' if the number if a multiple of 3 and 5
        otherwise, just print the number
    """

    for n in range(1,101):

        # multiple of 3 and 5
        if n % 3 == 0 and n % 5 == 0:
            print "FizzBuzz"

        # multiple of 3
        elif n % 3 == 0:
            print "Fizz"

        # multiple of 5
        elif n % 5 == 0:
            print "Buzz"

        # anything else
        else:
            print n

fizzbuzz()
