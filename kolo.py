from math import pi

def area(r):
    result = r ** 2 * pi
    return result


assert area(1) == pi

print(area(int(input('Enter radius of the circle: '))))

