def rectangleOverlap(rect1, rect2):
    """
    Determines of two rectangles overlap.
    Rectangles are given as lists of vertices, where each vertex is given as a tuple.
    
    Examples:

    >>> rectangleOverlap([(0,0), (0,5), (2,0), (2,5)], [(5,5), (5,7), (7,5), (7,7)])
    False

    >>> rectangleOverlap([(0,0), (0,5), (2,0), (2,5)], [(1,1), (1,2), (2,2), (2,1)])
    True

    >>> rectangleOverlap([(5,5), (5,7), (7,5), (7,7)], [(0,0), (0,5), (2,0), (2,5)])
    False

    >>> rectangleOverlap([(5,5), (5,7), (7,5), (7,7)], [(1,1), (1,2), (2,2), (2,1)])
    False
    """

    ## 1.
    r1_xs = []
    r1_ys = []
    for point in rect1:
        x = point[0]
        y = point[1]
        r1_xs.append(x)
        r1_ys.append(y)

    widthRange  = range( min(r1_xs), max(r1_xs) )
    heightRange = range( min(r1_ys), max(r1_ys) )

    ### 2. list comprehensions
    #r1_xs = [ p[0] for p in rect1 ]
    #r1_ys = [ p[1] for p in rect1 ]
    #widthRange  = range( min(r1_xs), max(r1_xs) )
    #heightRange = range( min(r1_ys), max(r1_ys) )

    ### 3. Slight cheat :)
    #widthRange  = range( rect1[1][0], rect1[2][0] )
    #heightRange = range( rect1[2][1], rect1[1][1] )

    for point in rect2:
        x = point[0]
        y = point[1]

        if x in widthRange and y in heightRange:
            return True

    return False
