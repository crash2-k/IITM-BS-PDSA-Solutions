# Goldbach's Conjecture

## Problem Statement

Goldbach's conjecture states that every even integer greater than 2 can be expressed as the sum of two prime numbers.

Write a function `Goldbach(n)` that accepts a positive even integer `n > 2` and returns a list of tuples `(a, b)` such that:

- `a` and `b` are prime numbers
- `a <= b`
- `a + b == n`

Each pair should appear once in the result.

## Examples

```python
Goldbach(12)  # [(5, 7)]
Goldbach(26)  # [(3, 23), (7, 19), (13, 13)]
```