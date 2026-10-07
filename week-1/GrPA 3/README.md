# Odd One Out

## Problem Statement

Write a function `odd_one(L)` that accepts a list `L`. Except for one element, all elements in `L` have the same data type. Return the data type of the odd element as a string.

The list has at least three elements, and the element types are among `int`, `float`, `str`, and `bool`.

## Examples

```python
odd_one([1, 2, 3.4, 5, 10])  # 'float'
odd_one([1, 2, 3, 'hello'])  # 'str'
```