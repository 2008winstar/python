number = 23
guess = int(input('Enter an integer: '))

# if...elif...else
if guess == number:
    pass
elif guess < number:
    pass
else:
    pass


# while
running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:
        pass
    else:
        pass
    running = False
else:
    # 可选，在while循环的条件为False时执行（如果while循环中没有break，这里总是会被执行
    pass


# for
for i in range(1, 5):
    print(i)
else:
    print('loop over')














