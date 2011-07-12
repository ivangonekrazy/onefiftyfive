def collatz(num):
    
    while num > 0:
        print num

        if num == 1:
            break

        if num % 2 == 1:
            num = num * 3 + 1
        elif num % 2 == 0:
            num = num / 2

if __name__ == "__main__":
    #collatz(1024)
    #collatz(50)
    collatz(10)
    #collatz(1)
    #collatz(0)
