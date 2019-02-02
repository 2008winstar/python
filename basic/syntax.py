# 布尔值
a = True
b = False


def get_para1(para=[], value=0):
    if para:
        para = []
    para.append(value)
    return para


get_para1()
