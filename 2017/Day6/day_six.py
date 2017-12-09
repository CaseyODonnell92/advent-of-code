import sys

def num_redistributions(banks, part_b = False):
    permutation_dict = {}

    permutation_dict[str(banks)] = 1
    redist_cycles = 0

    while True:
        max_index = banks.index(max(banks))
        max_val = banks[max_index]

        banks[max_index] = 0
        offset = 0
        while max_val > 0:
            offset += 1
            max_val -= 1
            banks[(max_index + offset) % len(banks)] += 1

        redist_cycles += 1
        if permutation_dict.get(str(banks), 0) > 0:
            if part_b:
                return num_redistributions(banks)
            return redist_cycles

        permutation_dict[str(banks)] = 1

if __name__ == "__main__":
    input_file = open("input.txt", 'r')
    banks = [int(num.strip()) for num in input_file.readline().split("\t")]
    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(num_redistributions(banks, True))
    else:
        print(num_redistributions(banks))
