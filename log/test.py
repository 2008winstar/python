import re

sum = 0
f = open('log.txt')
p = open('pro.txt', 'a')

for i in f:
    try:
        print(re.findall('{.*', i)[0])
    except BaseException as e:
        print(e)
