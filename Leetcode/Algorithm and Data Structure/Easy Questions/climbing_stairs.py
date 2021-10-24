def climbStairs(n):
    """ This makes use of Fibonacci Sequence algorithm. """
    a = b = 1
    for _ in range(n):
        # Start from left: a = b, then b = a + b
        a, b = b, a + b
    return a
