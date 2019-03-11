def devided_by57(start, end):
    return [num for num in range(start, end + 1) if num % 5 == 0 and num % 7 == 0]

r_start = 0
r_end = 0

while True:
    if not r_start:
        try:
            r_start = int(input('Enter range start: '))
        except ValueError:
            print('Invalid input')
            continue
    if not r_end:
        try:
            r_end = int(input('Enter range end: '))
        except ValueError:
            print('Invalid input')
            continue
    print(devided_by57(r_start, r_end))
    break
