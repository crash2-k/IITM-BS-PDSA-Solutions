def mergeInPlace(A, B):
    n = len(A)
    m = len(B)

    for i in range(n):
        if A[i] > B[0]:
            # swap and then move the swapped element to correct position in B
            A[i], B[0] = B[0], A[i]
            k = 0
            # bubble the new B[0] to its correct place to keep B sorted
            while k + 1 < m and B[k] > B[k + 1]:
                B[k], B[k + 1] = B[k + 1], B[k]
                k += 1


if __name__ == '__main__':
    try:
        A = list(map(int, input().strip().split()))
    except Exception:
        A = []
    try:
        B = list(map(int, input().strip().split()))
    except Exception:
        B = []

    mergeInPlace(A, B)

    print(' '.join(map(str, A)))
    print(' '.join(map(str, B)))
