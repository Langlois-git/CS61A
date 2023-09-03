from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    "*** YOUR CODE HERE ***"
    return sqrt((x1-x2)**2+(y1-y2)**2)

def harmonic(x, y):
    """Return the harmonic mean of x and y.

    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75

    """
    "*** YOUR CODE HERE ***"
    return 2 / (1/x + 1/y)

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    "*** YOUR CODE HERE ***"
    return sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)


def compare(a, b):
    """ Compares if a and b are equal.

    >>> compare(4, 2)
    'not equal'
    >>> compare(4, 4)
    'equal'
    """
    if a == b:
        return 'equal'
    return 'not equal'

def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1


    """
    "*** YOUR CODE HERE ***"
    x = x - 1
    while (x**(1/2)) % 1 != 0:
        x = x - 1
    return x

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    return low1 < min(high0, high1) > low0

def triangular_sum(n):
    """
    >>> t_sum = triangular_sum(5)
    1
    3
    6
    10
    15
    >>> t_sum
    35
    """
    "*** YOUR CODE HERE ***"
    t_num = 0 
    curr = 1
    total = 0
    while curr <= n:
        t_num = t_num + curr 
        total = total + t_num
        curr += 1
        print(t_num)
    return total

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
#    while a > 1:
#        print(a)
#        if a % 2 == 0:
#            a //= 2
#        else:
#            a = a * 3 + 1
#    return a
    def hailstone_check(a, b):
        while a > 1:
            if a == b:
                return True
            elif a % 2 == 0:
                a //= 2
            else:
                a = a * 3 + 1
        return False
    return  hailstone_check(a, b) or hailstone_check(b, a)

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    "*** YOUR CODE HERE ***"
    exponent = 0
    if x >= 2:
        while 2**exponent <= x:
            exponent += 1
        hp = (2**exponent)
        lp = (2**(exponent-1))
        if (hp - x) > (x - lp):
            return lp
        else:
            return hp
    else:
        while 2**exponent >= x:
            exponent -= 1
        hp = (2**(exponent+1))
        lp = 2**(exponent)
        if (hp - x) > (x - lp):
            return lp
        else:
            return hp

