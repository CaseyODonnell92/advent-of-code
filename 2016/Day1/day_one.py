distances = [0, 0, 0, 0]
direction = 0
visited = []

def absolute_val(num):
    if num < 0:
        return num * -1
    return num 

# For part 2
def get_coord(distances):
    coord = (distances[0] - distances[2], distances[1] - distances[3])
    return coord

def in_between(a, x, y):
    return (a >= x and a <= y) or (a <= x and a >= y)

instructions = [i for i in input().split(", ")]

for instr in instructions:
    if instr[0] == 'R':
        direction += 1
    else:
        direction -= 1

    direction = direction % 4
    revisited = False

    for i in range(0, int(instr[1:])):
        distances[direction] += 1

        coord = get_coord(distances)
        if coord in visited:
            revisited = True
            break
        else:
            visited.append(coord)

    if revisited:
        break

vert = absolute_val(distances[0] - distances[2])
horiz = absolute_val(distances[1] - distances[3])

print(vert + horiz)
    