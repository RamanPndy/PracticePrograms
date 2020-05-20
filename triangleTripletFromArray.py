def triplets(arr):
    n = len(arr)
    c = 0
    arr.sort()
    trip = []
    for i in range(n-2):

        k = i + 2

        for j in range(i+1 , n):

            while (k< n and arr[i] + arr[j] > arr[k]):
                k += 1

            if k > j:
                trip.append((arr[i], arr[j], arr[k-1]))
                c += k - j- 1

    return c, trip