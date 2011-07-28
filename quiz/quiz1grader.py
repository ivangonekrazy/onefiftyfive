import imp
import doctest
import sys

q = imp.load_source('quiz', sys.argv[1])

def _count_X(board):
    """
    """
    return q.count_X(board)

def _count_XO(board):
    """
    """
    return q.count_XO(board)

def _allowed_package(package):
    """
    """
    return q.allowed_package(package)

def _head_tail(l):
    """
    """
    return q.head_tail(l)

def _count_cubeX(bigcube):
    """
    >>> bigcube = [
            [['X','X','X'],['X','O','O'],['X','O','X']],
            [['X','O','O'],['X','O','X'],['X','X','X']],
            [['O','O','X'],['O','O','O'],['O','O','X']], 
        ]
    >>> count_cubeX(bigcube)
    14
    """
    pass
    return q.count_cubeX(bigcube)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
