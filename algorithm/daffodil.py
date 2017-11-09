def daffodil(num):
    """水仙花数: 153 = 1*1*1+5*5*5+3*3*3"""
    if 100 <= num <= 999:
        a = num // 100
        bc = num % 100
        b = bc // 10
        c = bc % 10
        # print(a, b, c)
        if num == a * a * a + b * b * b + c * c * c:
            print(num)


for i in range(100, 999):
    daffodil(i)
