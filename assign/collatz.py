def collatz(num):
    """
    Given a starting number, return the
    Collatz sequence as a list.

    >>> collatz(50)
    [50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    >>> collatz(16)
    [16, 8, 4, 2, 1]
    
    >>> collatz(10)
    [10, 5, 16, 8, 4, 2, 1]

    >>> collatz(0)
    []

    """
    sequence = []
    
    while num > 0:
        sequence.append(num)

        if num == 1:
            break

        if num % 2 == 1:
            num = num * 3 + 1
        elif num % 2 == 0:
            num = num / 2

    return sequence

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
