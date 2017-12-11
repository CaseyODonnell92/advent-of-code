import sys


def hash_num_array(lengths, num_list, index=0, skip=0):
    for length in lengths:
        inner_index = index

        for i in range(length//2):
            temp = num_list[inner_index]

            swap_index = (inner_index + length - 1 - i*2) % len(num_list)

            num_list[inner_index] = num_list[swap_index]
            num_list[swap_index] = temp

            inner_index = (inner_index + 1) % len(num_list)

        index = (index + length + skip) % len(num_list)
        skip += 1

    return index, skip


def full_hash(lengths, num_list, rounds):
    index = skip = 0

    for i in range(rounds):
        index, skip = hash_num_array(lengths, num_list, index, skip)

    hex_string = ""

    for i in range(0, len(num_list), 16):
        xor = num_list[i]

        inner_index = i + 1

        for j in range(15):
            xor = xor ^ num_list[inner_index]
            inner_index += 1

        hex_string += "{0:0>2}".format(hex(xor)[2:])

    return hex_string


if __name__ == "__main__":
    input_file = open("input.txt", 'r')

    num_list = [i for i in range(256)]

    input_string = input_file.read().strip()

    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        lengths = [int(char.encode("ascii")[0]) for char in input_string] + [17, 31, 73, 47, 23]

        print(full_hash(lengths, num_list, 64))
    else:
        lengths = [int(x) for x in input_string.split(',')]

        hash_num_array(lengths, num_list)
        print(num_list[0] * num_list[1])
