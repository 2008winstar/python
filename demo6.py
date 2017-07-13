l = [3, 1, 7, 4]

for i in range(len(l)):
    print('i', i)
    for j in range(i + 1, len(l)):
        print('j', j)
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
