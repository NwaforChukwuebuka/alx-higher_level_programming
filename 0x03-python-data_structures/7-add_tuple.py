#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples if they have less than 2 elements
    # or slice if they have more than 2 elements
    tuple_a = (
        tuple_a[0] if len(tuple_a) > 0 else 0,
        tuple_a[1] if len(tuple_a) > 1 else 0
    )
    tuple_b = (
        tuple_b[0] if len(tuple_b) > 0 else 0,
        tuple_b[1] if len(tuple_b) > 1 else 0
    )

    return tuple(map(sum, zip(tuple_a, tuple_b)))
