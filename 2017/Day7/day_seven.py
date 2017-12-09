import sys

def find_root_program(programs):
    progr_names = []
    child_progr_names = []

    for progr in programs:
        progr_names.append(progr)
        child_progr_names += programs[progr][1]

    for name in progr_names:
        if name not in child_progr_names:
            return name

def subtree_weight(programs, program):
    p = programs[program]
    weight = p[0]

    for child in p[1]:
        weight += subtree_weight(programs, child)

    return weight

def find_ideal_weight(programs, program, sibling_weight=0):
    child_sub_tree_weights = []
    for child in programs[program][1]:
        child_sub_tree_weights.append(subtree_weight(programs, child))

    # find unique weight - Assumption: one weight will be unique
    weight_count = {}
    for weight in child_sub_tree_weights:
        if weight_count.get(weight, 0) == 0:
            weight_count[weight] = 1
        else:
            weight_count[weight] += 1

    offender_index = 0
    all_sub_weights_equal = True
    for weight, count in weight_count.items():
        if count == 1:
            all_sub_weights_equal = False
            offender_index = child_sub_tree_weights.index(weight)

    if all_sub_weights_equal:
        return programs[program][0] + (sibling_weight - (subtree_weight(programs, program)))

    any_other_weight = child_sub_tree_weights[(offender_index + 1) % len(child_sub_tree_weights)]

    return find_ideal_weight(programs, programs[program][1][offender_index], any_other_weight)

if __name__ == "__main__":
    input_file = open("input.txt", 'r')

    programs = {}

    for line in input_file:
        line.strip()
        line_parts = line.split(" -> ")

        name_and_weight = line_parts[0].strip().split(" ")
        name = name_and_weight[0]
        weight = int(name_and_weight[1].strip()[1:-1])

        children = []

        if len(line_parts) == 2:
            children = line_parts[1].strip().split(", ")

        programs[name] = (weight, children)

    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(find_ideal_weight(programs, find_root_program(programs)))
    else:
        print(find_root_program(programs))
