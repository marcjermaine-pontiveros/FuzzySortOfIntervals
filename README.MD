# CS 210 Problem Set 2
## Fuzzy Sort of Intervals

Python implementation of Fuzzy sorting of intervals, making use of `namedtuples` to define intervals.

To use, define the list of intervals as follows:
```python

Interval = namedtuple('Interval', ['a', 'b'])
example = [Interval(3, 4), Interval(2.5, 4), Interval(1, 2), Interval(5, 9), Interval(2, 5), Interval(4.5, 6), Interval(7, 8)]

```

## References
[1] [Problem 7-6 of CLRS: Fuzzy Sorting of Intervals](https://walkccc.me/CLRS/Chap07/Problems/7-6/)
[2] [Quicksort Continued: Fuzzy Sorting](http://mypathtothe4.blogspot.com/2013/02/quicksort-continued-fuzzy-sorting.html)
[3] [CS 157 Paper of D.R. Lanman](https://alumni.media.mit.edu/~dlanman/courses/cs157/HW3.pdf)
