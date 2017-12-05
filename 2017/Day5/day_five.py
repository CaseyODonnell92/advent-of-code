import sys

def num_jumps(jumps, use_threshold=False, threshold=3):
    curr_index = last_index = jumps_num = 0
    while curr_index < len(jumps):
        last_index = curr_index
        curr_index += jumps[curr_index]
        jumps_num += 1

        if threshold and jumps[last_index] >= threshold:
            jumps[last_index] -= 1
        else:
            jumps[last_index] += 1

    return jumps_num

if __name__ == "__main__":
    input_file = open("input.txt")
    jumps = [int(line.strip()) for line in input_file]
    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(num_jumps(jumps, True))
    else:
        print(num_jumps(jumps))
