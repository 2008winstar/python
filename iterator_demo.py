my_list = [1, 2, 3]


def map_item(item):
    return item * 2

your_list = map(map_item, my_list)
print(your_list)
