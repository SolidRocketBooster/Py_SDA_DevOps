
def missing(list_check, max):
    return list(set(range(1, max + 1)) - set(list_check))

x = [1, 2, 4, 5, 7, 10 , 11, 15, 18, 19]

l = missing(x, 20)
print(l)
