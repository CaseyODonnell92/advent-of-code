import sys

def sum_matching_numbers(nums, interval):
    sum = 0
    for i in range(0, len(nums)):
        if nums[i] == nums[(i + interval) % len(nums)]:
            sum += int(nums[i])
    return sum

if __name__ == "__main__":
    nums = open("input.txt").read()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(sum_matching_numbers(nums, len(nums)//2))
    else:
        print(sum_matching_numbers(nums, 1))
    