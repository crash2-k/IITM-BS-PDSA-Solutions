def findLargest(L):
    left = 0
    right = len(L) - 1

    while left < right:
        mid = (left + right) // 2

        if L[mid] > L[mid + 1]:
            return L[mid]
        if L[mid] >= L[left]:
            left = mid + 1
        else:
            right = mid

    return L[left]


L = list(map(int, input().split()))
print(findLargest(L))
