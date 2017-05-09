input_number = input('enter a series of number: ')
number_list = input_number.split(' ')
number_list.sort()
print(number_list)
if len(number_list) % 2 == 1:
    print(number_list[int((len(number_list) - 1) / 2)])

print(help(map))

