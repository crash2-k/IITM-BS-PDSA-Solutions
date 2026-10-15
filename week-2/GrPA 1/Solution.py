def combinationSort(strList):
    L1 = sorted(strList, key=lambda value: value[0])
    L2 = sorted(strList, key=lambda value: (value[0], -int(value[1:])))
    return L1, L2


strList = [value.strip() for value in input().split(",")]
L1, L2 = combinationSort(strList)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))
