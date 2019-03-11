# def spam(i, x, y, l = 123, *args, **kwargs):
#     print(i, x, y, l)
#     print(args)
#     print(kwargs)
#
#
# spam(1, 2, 3, 4, 4, 4)
# spam(1, y=2, x=10)
# spam(1, 2, 3, 4, 5, 43234, 32, dupa=True, piwo=True)

s1 = {'piwo': 1}
s2 = {'fajki': 4}

s3 = {**s1, **s2}

print(s3)
