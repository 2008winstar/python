it = input('enter your numbers: ')
lt = it.split(' ')


# lt[8] = 7

print(lt)
def tongpaixu(lt):
    lt = [int(i) for i in lt]
    l = max(lt) + 1
    new_lt = []
    for i in range(l):
        new_lt.append(0)
    # print(new_lt)
    for i in lt:
        new_lt[i] = i

    # print(new_lt)
    for i in new_lt:
        if i != 0:
            print(i, end=' ')


tongpaixu(lt)

# print(lt)
