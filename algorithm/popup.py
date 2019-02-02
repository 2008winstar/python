it = input('input your numbers: ')
lt = it.split(' ')
lt = [int(i) for i in lt]


def pop(lt):
    for i in range(len(lt)):
        for j in range(i + 1, len(lt)):
            if lt[i] < lt[j]:
                lt[i], lt[j] = lt[j], lt[i]
    print(lt)


pop(lt)
