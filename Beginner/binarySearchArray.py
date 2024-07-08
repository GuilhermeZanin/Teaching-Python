# Given a sorted array, find the index of the first element ≥ X (return -1 if no element ≥ X).
def lower_bound(array: list[int], X: int) -> int:
    n = len(array)
    if array[n-1] < X:
        return -1
    if array[0] >= X:
        return 0

    lo = 0
    hi = n-1

    while lo+1 < hi:
        mid = (lo+hi) // 2	
        if array[mid] < X:
            lo = mid
        else:
            hi = mid
    return hi


print(lower_bound([1,2,3,4,5,6,7,8], 2))