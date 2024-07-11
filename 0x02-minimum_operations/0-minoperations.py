#!/usr/bin/python3
"""
File contains function minOperations
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the
    file

    Args:
        n: number of H characters

    Returns:
        number of operations
    """
    operations = 0
    current: str = "H"
    value: str = "H"
    while len(current) < n:
        if n % len(current) == 0:
            operations += 2
            value = current
            current += current
        else:
            operations += 1
            current += value

    if len(current) != n:
        return 0
    return operations
