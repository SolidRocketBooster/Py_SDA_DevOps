list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even(l):
    n_l = []
    for i in l:
        if i % 2 == 0:
            n_l.append(i)
    return n_l


print(even(list))

nl = [x for x in list if x % 2 == 0]
print(nl)
