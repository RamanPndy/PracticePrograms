def spiralOrder(mat):
    if not mat:
        return []
    res = []
    while mat:
        res.extend(mat.pop(0))
        if mat and mat[0]:
            for row in mat:
                res.append(row.pop())
        if mat:
            res.extend(mat.pop()[::-1])
        if mat and mat[0]:
            for row in mat[::-1]:
                res.append(row.pop(0))
    return res

a = [[1,2,3],[4,5,6],[7,8,9]]
print (spiralOrder(a))
