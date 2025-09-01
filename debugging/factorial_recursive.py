#!/usr/bin/python3
import sys


def factorial(n):
    """
    Fonction description:
        Recursively calculates the factorial of a non-negative integer n.

    Parameters:
        n : int

    Returns:
        int
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
