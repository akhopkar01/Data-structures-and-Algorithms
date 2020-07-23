def sqrt(n):
    # Edge case 1
    if n == 0:
        return 0

    # Edge case 2
    if n < 0:
        return None

    # Iterative solution -  Complexity: O(sqrt(n))
    for i in range(1, n+1):
        if i == n//i:
            return i


if __name__ == "__main__":
    print(sqrt(9))
    print(sqrt(4))
    print(sqrt(25))
    print(sqrt(49))
    print(sqrt(52))
    print(sqrt(27))
    print(sqrt(225))
    print(sqrt(110))
    print(sqrt(0))
    print(sqrt(-25))
    print(sqrt(1))