def findMinSwap(arr, n):
    # Declare a vector of pair
    vec = []

    for i in range(n):
        vec.append([arr[i], i])

        # Sort the vector w.r.t the first
    # element of pair
    vec = sorted(vec)

    ans, c, j = -1, 0, 0

    for i in range(n):

        # If the element is already placed
        # correct, then continue
        if (vec[i][1] == i):
            continue
        else:
            # swap with its respective index
            vec[i][0], vec[vec[i][1]][1] = vec[vec[i][1]][1], vec[i][0]
            vec[i][1], vec[vec[i][1]][1] = vec[vec[i][1]][1], vec[i][1]

            # swap until the correct
        # index matches
        if (i != vec[i][1]):
            i -= 1

        # each swap makes one element
        # move to its correct index,
        # so increment answer
        ans += 1

    return ans