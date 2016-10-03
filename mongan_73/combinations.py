import copy


def print_combinations_recursive_top(word):
    print_combinations_recursive(word, [])


def print_combinations_recursive(word, state):
    if len(state) == len(word):
        out = ''
        for i in range(len(word)):
            if state[i]:
                out += word[i]
        print out
    else:
        for b in (0, 1):
            new_state = copy.deepcopy(state)
            new_state.append(b)
            print_combinations_recursive(word, new_state)