# 字符串格式化
age = 20
name = 'Swaroop'

# format 格式化方法
print('{0} was {1} years old when he wrote this book.'.format(name, age))
# 数字是可选的
print('{} was {} years old when he wrote this book.'.format(name, age))

# 详细格式
# 对于浮点数0.333保留小数点后3位
print('{0:.3f}'.format(1/3))
# 使用^定义字符串长度
# 使用下划线填充文本，并保持文字处于中间位置
print('{0:_^11}'.format('hello'))
# 基于关键词
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# print总是会新起一行，可以通过end参数指定行尾结束内容
print(3, end='')
