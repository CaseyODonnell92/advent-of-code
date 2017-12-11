import sys


def get_stream_score(stream):
    group_count = 0
    score = 0
    garbage_chars = 0

    state_stack = []

    i = 0

    while i < len(stream):
        state = "default"
        if len(state_stack) > 0:
            state = state_stack[-1]

        if state == "default":
            if stream[i] == '<':
                state_stack.append("garbage")
            elif stream[i] == '{':
                group_count += 1
                state_stack.append("group")
        elif state == "group":
            if stream[i] == '{':
                group_count += 1
                state_stack.append("group")
            elif stream[i] == '}':
                score += group_count
                group_count -= 1
                state_stack.pop()
            elif stream[i] == '<':
                state_stack.append("garbage")
        elif state == "garbage":
            if stream[i] == '!':
                i += 1
            elif stream[i] == '>':
                state_stack.pop()
            else:
                garbage_chars += 1

        i += 1

    return (score, garbage_chars)

if __name__ == "__main__":
    input_file = open("input.txt", 'r')

    stream = input_file.read().strip()

    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(get_stream_score(stream)[1])
    else:
        print(get_stream_score(stream)[0])