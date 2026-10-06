def Goldbach(n):
    def is_prime(number):
        if number < 2:
            return False
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                return False
        return True

    result = []
    for first in range(2, n // 2 + 1):
        second = n - first
        if is_prime(first) and is_prime(second):
            result.append((first, second))
    return result


n = int(input())
print(sorted(Goldbach(n)))