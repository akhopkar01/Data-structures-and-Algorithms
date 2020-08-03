
def sqrt(n):
    if n == 0 or n == 1:
        return n

    if n < 0:
        return None

    start = 0
    end = n

    return _find_root(n, start, end)

def _find_root(n, start, end):
    mid = (start+end) // 2
    mid_sq = mid*mid

    if mid_sq == n or abs(mid_sq-n) < 5:
        return mid

    elif mid_sq < n:
        return _find_root(n, mid+1, end)

    else:
        return _find_root(n, start, mid-1)



if __name__ == "__main__":
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (7 == sqrt(53)) else "Fail")