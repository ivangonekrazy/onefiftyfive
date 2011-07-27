import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: %s, y:%s" % (self.x, self.y)

    def __len__(self):
        return 1

    def distFromOrigin(self):
        return math.sqrt( self.x**2 + self.y**2 )

p = Point(4,3)
print p 
print p.x, p.y
print p.distFromOrigin()
print len(p)

p2 = Point()
print p2
print p2.x, p2.y
print p2.distFromOrigin()
print len(p2)
