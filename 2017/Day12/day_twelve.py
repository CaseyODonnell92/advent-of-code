import sys


def group_connected_by_program(program_connectivities, program):
    visited = set()

    traversal_stack = [program]

    while len(traversal_stack) > 0:
        visit = traversal_stack.pop()
        visited.add(visit)

        for neighbour in program_connectivities[visit]:
            if neighbour not in visited:
                traversal_stack.append(neighbour)

    return visited


if __name__ == "__main__":
    input_file = open("input.txt", 'r')

    program_connectivities = {}

    for line in input_file:
        line_parts = line.strip().split(" <-> ")

        program_connectivities[int(line_parts[0])] = [int(x) for x in line_parts[1].split(", ")]

    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        group_count = 0

        while len(program_connectivities) > 0:
            group = group_connected_by_program(program_connectivities, list(program_connectivities.keys())[0])

            for program in group:
                del program_connectivities[program]

            group_count += 1

        print(group_count)
    else:
        print(len(group_connected_by_program(program_connectivities, 0)))
