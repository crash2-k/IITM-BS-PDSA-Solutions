# Find Minimum Difference

## Problem Statement

Write a function `find_Min_Difference(L, P)` that accepts:

- `L`: a list of integers
- `P`: a positive integer

The size of `L` is greater than `P`.

The task is to select `P` different elements from the list `L` such that the difference between the maximum and minimum selected values is as small as possible.

The function should return this minimum difference.

> **Note:** The list can contain more than one subset of `P` elements having the same minimum difference.

---

## Example

Consider:

```python
L = [3, 4, 1, 9, 56, 7, 9, 12, 13]
P = 5