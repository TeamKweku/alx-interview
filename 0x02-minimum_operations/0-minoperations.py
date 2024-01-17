#!/usr/bin/python3
"""module that implements a solution for the popular interview question"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to
    obtain n 'H' charactersin a text file using 'Copy All' and 'Paste'
    operations.

    Parameters:
    - n (int): The target number of 'H' characters.

    Returns:
    - int: The minimum number of operations required.
    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    len_of_H = 1
    len_of_copied_H = 0
    total_operations = 0

    while len_of_H < n:
        if n % len_of_H == 0:
            # Perform "Copy All" and "Paste" operations
            total_operations += 2
            len_of_copied_H = len_of_H
            len_of_H *= 2
        else:
            # Increment length by the value of copied length and
            # perform "Paste" operation
            total_operations += 1
            len_of_H += len_of_copied_H

    return total_operations
