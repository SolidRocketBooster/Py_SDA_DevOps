
def new_list():
    n_list = []
    for num in range(4, 12):
        n_list.append(num * 0.5)
    return n_list

def new_list2(n, m, s=0.5):
    n_list = []
    i = n
    while i <= m:
        n_list.append(i)
        i += s
    return n_list

print(new_list())
print(new_list2(2, 5.5))
