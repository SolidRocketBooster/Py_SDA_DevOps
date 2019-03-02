def to_f(temp):
    return round(temp * 9/5 + 32, 2)


assert to_f(0) == 32
assert to_f(5) == 41
