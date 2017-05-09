left_set = ['{', '[', '(']
right_set = [')', ']', '}']
left = []
right = []
txt = '({})[{]'
for i in txt:
    if i in left_set:
        left.append(i)
    elif i in right_set:
        if i == ')':
            if left.pop() == '(':
                continue
            else:
                print 'error'
                break
        if i == ']':
            if left.pop() == '[':
                continue
            else:
                print 'error'
                break
        if i == '}':
            if left.pop() == '{':
                continue
            else:
                print 'error'
                break

