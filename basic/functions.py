def say_hello():
    print('hi')


say_hello()

# 传参
# 局部变量
# 全局变量 global


def say(message, times=1):
    """默认参数值示例"""
    print(message*times)


def func(a, b=5, c=10):
    """关键字参数示例"""
    print('a is ', a, ' and b is ', b, ' and c is ', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


def total(a=5, *numbers, **phonebook):
    """可变参数示例"""
    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))














