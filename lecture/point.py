import math

"""
    Example of how to build a class.
"""

class Point(object):
    """
        Defines a class to represent a point
        in space with an X and Y coordinate.

        Functions inside of a class that begin and end
        with __ (double-underscore) are called "special methods"
        in Python.
    """

    # this object will have an x and y coordinate
    # that can be accessed by object.x and object.y
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        """
        The initializer special method. When an object is 
        first created from a class, this function is automatically called.
        This particular function uses default arguments, so if and x and
        y are not provided, we will assume they are both 0.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        There are many special methods available in Python. 
        This one tells Python how to convert objects of this class
        to strings when the need arises. For example whenever
        we 'print' this object, Python will ask this function
        for the string representation of this classes objects.
        """
        return "x: %s, y:%s" % (self.x, self.y)

    def __len__(self):
        """
        Likewise for this one. Whenever Python needs to know the
        length of this object, this function is called
        """
        return 1

    def distFromOrigin(self):
        """
        This is a user-defined method. We look into this
        object for its X and Y coordinate and return this points
        distance from origin (0,0).
        """
        return math.sqrt( self.x**2 + self.y**2 )

# build a new object of class Point
# have that Points X be 4 and Y be 3
p = Point(4,3)
print p 
print p.x, p.y
print p.distFromOrigin()
print len(p)

# build a new object of class Point
# let the X and Y default to 0
p2 = Point()
print p2
print p2.x, p2.y
print p2.distFromOrigin()
print len(p2)
