from random import randint
from collections import namedtuple
# Define interval data structure
Interval = namedtuple('Interval', ['a', 'b'])

l_intervals = [Interval(1, 3), Interval(2, 5), Interval(1, 6), Interval(1, 7)]
example = [Interval(3, 4), Interval(2.5, 4), Interval(1, 2), Interval(5, 9), Interval(2, 5), Interval(4.5, 6), Interval(7, 8)]


def find_intersection(A, p, r):
    rand = randint(p, r)
    A[rand], A[r] = A[r], A[rand]
    a = A[r].a 
    b = A[r].b
    for i in range(p, r):
        if A[i].a <= b and A[i].b >= a:
            if A[i].a > a:
                a = A[i].a 
            if A[i].b < b:
                b = A[i].b
    return (a, b)

def partition_left(A, b, p, t):
    i = p - 1
    for j in range(p, t):
        if A[j].b < b:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[t] = A[t], A[i+1]
    return i+1

def partition_right(A, a, p, r):
    i = p - 1
    for j in range(p, r):
        if A[j].a <= a:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def fuzzy_sort(intervals):
    fuzzy_sortI(intervals, 0, len(intervals) - 1)

def fuzzy_sortI(A, p, r):
    if p < r:
        (a, b) = find_intersection(A, p, r)
        t = partition_right(A, a, p, r)
        q = partition_left(A, b, p, t)
        fuzzy_sortI(A, p, q - 1)
        fuzzy_sortI(A, t + 1, r)

#print(find_intersection(l_intervals, 0, len(l_intervals)-1))
#fuzzy_sort(l_intervals, 0, len(l_intervals)-1)
#print(l_intervals)
fuzzy_sort(example)

print(example)