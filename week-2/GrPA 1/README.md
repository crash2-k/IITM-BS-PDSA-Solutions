# Combination Sort

## Problem Statement

Write a function `combinationSort(strList)` that accepts a list of unique
strings. Each string consists of a lowercase letter followed by a number from
`0` to `99`.

Return two lists:

- `L1`: Sort by the first character in ascending order, preserving the original
  order of strings with the same first character.
- `L2`: Sort by the first character in ascending order, then by the numeric
  portion in descending order.

## Example

```text
Input:
d34, g54, d12, b87, g1, c65, g40, g5, d77

Output:
L1: b87, c65, d34, d12, d77, g54, g1, g40, g5
L2: b87, c65, d77, d34, d12, g54, g40, g5, g1
```
