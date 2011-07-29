
def head_tail(l):
    # note that t here is a tuple
    # l[0] is the first element, the head
    # l[1:] is the slice of the list from
    # index 1 onwards; index 0 not included
    t = ( l[0], l[1:] )
    return t

# think of the board list as
# - a list of rows
# - each row is a list of cells
board = [
    ['X','O','X'],
    ['O','O','X'],
    ['X','X','O']
]

def count_X(t):
    numX = 0
    for row in t:
        #print "Looking at row: %s" % row
        for cell in row:
            #print "Looking at cell: %s" % cell
            if cell == 'X':
                numX = numX + 1
    return numX

def count_XO(t):
    numDict = {'X':0, 'O':0 }
    for row in t:
        for cell in row:
            if cell == 'X':
                numDict['X'] = numDict['X'] + 1
            if cell == 'O':
                numDict['O'] = numDict['O'] + 1
    return numDict

package= {"weight": 12, "height":8, "width": 8, "depth": 8}
def allowed_packages(p):

    weight = p['weight']
    width = p['width']
    height = p['height']
    depth = p['depth']

    # check weight
    if weight > 15:
        return False

    # check volume
    volume = height * width * depth
    if volume > 1000:
        return False

    # check dimensions
    if width > 20: 
        return False
    if height > 20:
        return False
    if depth > 20:
        return False

    # another way to do the dimension check
    # all in one condition
    if width > 20 or height > 20 or depth > 20:
        return False

    # if any of the previous conditions were True
    # then their return False would have ended
    # this function

    # if we get this far, that means all the previous
    # conditions were False, which means our package
    # didn't hit any of the restrictions
    # we can safely conclude that our package is 
    # ready to send by returning True
    return True

