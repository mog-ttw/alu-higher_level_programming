#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, padding with 0 if necessary
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Return new tuple with sum of first two elements from each tuple
    return (a[0] + b[0], a[1] + b[1])
