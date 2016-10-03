import copy




def print_perms_recursive_top(word):
    print_perms_recursive(word, [])


def print_perms_recursive(word, perm):

    if len(perm) == len(word):
        out = ''
        for i_letter in perm:
            out += word[i_letter]
        print out

    else:
        for i_letter in range(len(word)):
            if i_letter not in perm:
                new_perm = copy.deepcopy(perm)
                new_perm.append(i_letter)
                print_perms_recursive(word, new_perm)