import sys

def find_min_distance_to_centre(num):
    if num <= 1:
        return 0
    i = 1
    square = 1
    while num > square:
        i += 2
        square = i**2
    return i - 1 - ((square - num) % (i - 1))

def add_adjacent_spiral_blocks(spiral, coords):
    sum = 0
    for i in range(coords[0] - 1, coords[0] + 2):
        for j in range(coords[1] - 1, coords[1] + 2):
            if i == coords[0] and j == coords[1]:
                continue
            coord_str = str(i) + "," + str(j)
            block = spiral.get(coord_str, 0)
            sum += block
    return sum

def part_two(num):
    spiral = {"0,0":1}

    if num <= 1:
        return spiral["0,0"]

    coords = [0, 0]
    index = [0, 1] 
    steps = 1
    incr = 1
    block_num = 1

    while True:
        for i in range(0, 2):
            for j in range(0, steps):
                block_num += 1
                coords[index[0]] += incr
                coord_str = str(coords[0]) + "," + str(coords[1])
                new_block = add_adjacent_spiral_blocks(spiral, coords)
                spiral[coord_str] = new_block
                if new_block > num:
                    return new_block
            index.reverse()
        steps += 1
        incr *= -1

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(part_two(int(input())))
    else:
        print(find_min_distance_to_centre(int(input())))
    