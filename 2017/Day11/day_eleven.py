import sys


def direction_value(direction):
    if direction == 'n' or direction == 'e':
        return 1
    if direction == 's' or direction == 'w':
        return - 1


def trace_path(directions):
    horiz = vert = 0

    max_vert = max_horiz = 0

    for direction in directions:
        vert += direction_value(direction[0])

        if len(direction) > 1:
            horiz += direction_value(direction[1])

        if abs(vert) > max_vert:
            max_vert = abs(vert)
        if abs(horiz) > max_horiz:
            max_horiz = abs(horiz)

    horiz = abs(horiz)
    vert = abs(vert)

    return (vert, horiz), (max_vert, max_horiz)


def shortest_hexagonal_distance(coord):
    vert, horiz = coord

    count = 0

    while horiz > 0:
        if vert > 0:
            vert -= 1
            horiz -= 1
            count += 1
        else:
            break

    return count + horiz + (vert//2 + (vert % 2))

if __name__ == "__main__":
    input_file = open("input.txt", 'r')

    directions = [x for x in input_file.read().strip().split(',')]

    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(shortest_hexagonal_distance(trace_path(directions)[1]))
    else:
        print(shortest_hexagonal_distance(trace_path(directions)[0]))
