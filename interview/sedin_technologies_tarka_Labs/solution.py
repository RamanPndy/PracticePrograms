map = {
    1: ["Z", "N"],
    2: ["M", "C", "D"],
    3: ["P"]
}

instructions = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]

for ins in instructions:
    instruction = ins.split(" ")
    n, f, t = int(instruction[1]), int(instruction[3]), int(instruction[5])
    source = map[f]
    for j in range(n):
        map[t].append(source.pop())

print (map)