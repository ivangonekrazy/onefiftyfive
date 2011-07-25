import random

def randomGame(n):
    number = random.randint(0,n)

    print "I'm thinking of a number between 0 and %s" % n
    print "Can you guess what it is?"
    print "Type 'quit' to quit."

    guesses = []
    try:
        while True:
            userinput = raw_input("Guess > ")

            if userinput == "quit":
                print "The number was %s, you quitter!" % number
                break
            elif userinput in guesses:
                print "You've already guessed that!"
            elif int(userinput) == number:
                print "Congratulations!"
                break
            else:
                guesses.append(userinput)

    except ValueError:
        print "You're not playing by the rules!"

randomGame(10)

