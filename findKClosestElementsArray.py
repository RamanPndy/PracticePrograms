def findKClosestElementsArray(arr, k, x):
    sortedarr = sorted(arr)
    n = len(sortedarr)
    if (x <= sortedarr[0]):
        return arr[:k]
    if (x >= sortedarr[n - 1]):
        return arr[n - k:]
    low, high = 0, n - k
    while low < high:
        mid = (low + high) // 2
        if x - arr[mid] > arr[mid + k] - x:
            low = mid + 1
        else:
            high = mid
    return arr[low:low + k]
