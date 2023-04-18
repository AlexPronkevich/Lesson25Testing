alfabet = ['a', 'b', 'c', 'd', 'e']
counts = [10, 34, 23, 17, 56]

for i in range(len(counts) - 1):
    for j in range(len(counts) - 1 - i):
        if counts[j] < counts[j + 1]:
            temp = counts[j]
            counts[j], counts[j + 1] = counts[j + 1], counts[j]
            alfabet[j], alfabet[j + 1] = alfabet[j + 1], alfabet[j]

print(alfabet)
print(counts)
