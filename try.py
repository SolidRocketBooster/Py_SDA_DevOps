try:
    a = int(input('Enter your number: '))
except ValueError:

try:
    print(10/a)
except ZeroDivisionError:
    print('Invalid number!')

print('Rest of the script')
