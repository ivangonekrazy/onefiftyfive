#!/usr/bin/python
import imp
import doctest
import sys

q = imp.load_source('quiz', sys.argv[1])

def _count_X(board):
    """
    >>> _count_X([ ['X','O','X'], ['O','O','X'], ['X','X','O'] ])
    5
    >>> _count_X([ ['X','X','X'], ['X','X','X'], ['X','X','X'] ])
    9
    >>> _count_X([ ['O','O','O'], ['X','X','X'], ['O','O','O'] ])
    3
    >>> _count_X([ ['O','O','O'], ['O','O','O'], ['O','O','O'] ])
    0
    """
    return q.count_X(board)

def _count_XO(board):
    """
    >>> d = _count_XO([ ['X','O','X'], ['O','O','X'], ['X','X','O'] ])
    >>> d['X'] == 5 and d['O'] == 4
    True
    >>> d = _count_XO([ ['X','X','X'], ['X','X','X'], ['X','X','X'] ])
    >>> d['X'] == 9 and d['O'] == 0
    True
    >>> d = _count_XO([ ['O','O','O'], ['X','X','X'], ['O','O','O'] ])
    >>> d['X'] == 3 and d['O'] == 6
    True
    >>> d = _count_XO([ ['O','O','O'], ['O','O','O'], ['O','O','O'] ])
    >>> d['X'] == 0 and d['O'] == 9
    True
    """
    return q.count_XO(board)

def _allowed_package(package):
    """
    >>> _allowed_package( {"weight": 12, "height":8, "width": 8, "depth": 8} )
    True
    >>> _allowed_package( {"weight": 20, "height":8, "width": 8, "depth": 8} )
    False
    >>> _allowed_package( {"weight": 2, "height":2, "width": 2, "depth": 30} )
    False
    >>> _allowed_package( {"weight": 10, "height":6, "width": 10, "depth": 20} )
    False
    >>> _allowed_package( {"weight": 10, "height":60, "width": 2, "depth": 2} )
    False
    >>> _allowed_package( {"weight": 10, "height":2, "width": 60, "depth": 2} )
    False
    >>> _allowed_package( {"weight": 10, "height":2, "width": 2, "depth": 60} )
    False
    >>> _allowed_package( {"weight": 10, "height":2, "width": 2, "depth": 2} )
    True
    """
    return q.allowed_package(package)

def _head_tail(l):
    """
    >>> _head_tail( [1,2,3,4] )
    (1, [2, 3, 4])
    >>> _head_tail( [4,4,4,4] )
    (4, [4, 4, 4])
    >>> _head_tail( ['x','x','x','x'] )
    ('x', ['x', 'x', 'x'])
    >>> _head_tail( ['head', 'tail', 'tail', 'tail'] )
    ('head', ['tail', 'tail', 'tail'])
    """
    return q.head_tail(l)

def _count_cubeX(bigcube):
    """
    >>> bigcube = [
    ... [['X','X','X'],['X','O','O'],['X','O','X']],
    ... [['X','O','O'],['X','O','X'],['X','X','X']],
    ... [['O','O','X'],['O','O','O'],['O','O','X']],
    ... ]
    >>> _count_cubeX(bigcube)
    14
    >>> bigcube = [
    ... [['X','X','X'],['X','X','X'],['X','X','X']],
    ... [['X','X','X'],['X','X','X'],['X','X','X']],
    ... [['X','X','X'],['X','X','X'],['X','X','X']],
    ... ]
    >>> _count_cubeX(bigcube)
    27
    """
    return q.count_cubeX(bigcube)

if __name__ == "__main__":
    print "Checking %s ..." % sys.argv[1]
    doctest.testmod()
