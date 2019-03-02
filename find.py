i = 1500
list = []
while i <= 2700:
    if i % 5 == 0 and i % 7 == 0:
        list.append(i)
    i += 1

print(*list)

print([l for l in range(1500, 2701) if l % 5 == 0 and l % 7 == 0])