start, end = '79-900', '80-155'

print(['-'.join([num[:2], num[2:]]) for num in range(int(start.replace('-', '')) + 1, int(end.replace('-', '')))])
