def solution(h, w, queries):
    grid = [[0 for i in range(w)] for j in range(h)]
    output = []
    for query in queries:
        token = query.split(" ")
        direction, row, col = token[0], int(token[1]), int(token[2])
        if direction == "x":
            grid[row][col] = 1
        else:
            res = [-1, -1]
            if direction == ">":
                for i in range(col + 1, w):
                    if grid[row][i] == 0:
                        res[0] = row
                        res[1] = i
                        break
            elif direction == "<":
                for i in range(col - 1, 0, -1):
                    if grid[row][i] == 0:
                        res[0] = row
                        res[1] = i
                        break
            elif direction == "v":
                for i in range(row +1, h):
                    if grid[i][col] == 0:
                        res[0] = i
                        res[1] = col
                        break
            elif direction == "^":
                for i in range(row -1, 0, -1):
                    if grid[i][col] == 0:
                        res[0] = i
                        res[1] = col
                        break
            output.append(res)
    return output