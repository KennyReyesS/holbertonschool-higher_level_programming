#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupcpy_a = tuple_a + (0, 0)
    tupcpy_b = tuple_b + (0, 0)
    tupcpy_a = tupcpy_a[:2]
    tupcpy_b = tupcpy_b[:2]

    return(tuple(map(sum, zip(tupcpy_a, tupcpy_b))))
