import sys


def parse_instructions(input_file):
    instructions = []

    for line in input_file:
        op_and_condition = line.strip().split(" if ")

        op = op_and_condition[0].split()

        num = int(op[2])

        if op[1] == "dec":
            num *= -1

        cond = op_and_condition[1].split()

        cond_string = cond[1] + " " + cond[2]

        instructions.append(((op[0], num), (cond[0], cond_string)))

    return instructions


def execute_instructions(instructions, registers):
    max_val = 0

    for instruction in instructions:
        if eval(str(registers.get(instruction[1][0], 0)) + " " + instruction[1][1]):
            if registers.get(instruction[0][0], 0) == 0:
                registers[instruction[0][0]] = 0

            registers[instruction[0][0]] += instruction[0][1]

            if registers[instruction[0][0]] > max_val:
                max_val = registers[instruction[0][0]]

    return max_val

if __name__ == "__main__":
    input_file = open("input.txt")

    registers = {}

    instructions = parse_instructions(input_file)
    input_file.close()

    max_val = execute_instructions(instructions, registers)

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(max_val)
    else:
        reg_vals = list(registers.items())

        max_reg = reg_vals[0]

        for i in range(1, len(reg_vals)):
            if reg_vals[i][1] > max_reg[1]:
                max_reg = reg_vals[i]

        print(max_reg[1])
