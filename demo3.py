n = 1000
while n < 9999:
    if n % 4 == 0:
        m = n // 10
        if m % 3 == 0:
            x = m // 10
            if x % 2 == 0:
                print(n)
    n += 1

name = input()
