numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def average(l):
    return sum(l)/len(l)


print(average(numberList))

from statistics import mean
print(mean(numberList))
