import sys

def find_max_min_diffs(input_file, diffs):
    for line in input_file:
        nums = [int(num) for num in line.split("\t")]
        line_min = line_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < line_min:
                line_min = nums[i]
            if nums[i] > line_max:
                line_max = nums[i]
        diffs.append(line_max - line_min)

def find_divisible_pairs(input_file, diffs):
    for line in input_file:
        nums = [int(num) for num in line.split("\t")]

        for i in range(0, len(nums) - 1):
            found = False

            for j in range(i + 1, len(nums)):
                pair = [nums[i], nums[j]]
                pair.sort()
                quot = pair[1] / pair[0]
                if quot % 1 == 0:
                    diffs.append(int(quot))
                    found = True
                    break

            if found:
                break

if __name__ == "__main__":
    input_file = open("input.txt",'r')

    diffs = []
    
    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        find_divisible_pairs(input_file, diffs)
    else:
        find_max_min_diffs(input_file, diffs)

    input_file.close()

    checksum = diffs[0]
    for i in range (1, len(diffs)):
        checksum += diffs[i]

    print(checksum)
    