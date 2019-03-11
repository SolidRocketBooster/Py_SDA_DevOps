import random

def random_list(n):
    set = []
    for i in range(0, n):
        set.append('[')
        set.append(']')
    random.shuffle(set)
    return set


def check(list_random):
    i = 0
    while len(list_random) >= 2:
        if list_random[i] == '[' and list_random[i + 1] == ']':
            list_random.pop(i)
            list_random.pop(i+1)
        else:
            i += 1

    if list_random == [']', '[']:
        return 'NOT OK'
    else:
        return 'OK'

n_list = random_list(10)
print(n_list)

print(check(n_list))