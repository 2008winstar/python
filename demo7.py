import sys


def unique_list(a_list):
    return list(set(a_list[:]))

lst = [1, 2, 3, 3, 5, 7, 8, 2, 1, 8]
print(unique_list(lst))

dt = {
    'abc': 3
}

print(dt.get('abc'))

print(sys.getrefcount(5))
