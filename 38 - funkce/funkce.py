# def obvod_trojuhelnika(a,b,c):
#     d = a + b + c
#     return d

# result = obvod_trojuhelnika(15,18,20)
# print(result)

# ---------------------------------------------------

import math

def  obvod_kruhu(r):
    return (2 * math.pi * r)


result = obvod_kruhu(20)
print(result)


def obsah_kruhu(r):
    return math.pi * (r * r)


result2 = obsah_kruhu(10)
print(result2)


def get_quadrangle_type(a,b,c,d):
    if a == b == c == d:
        print("Je to čtverec.")
    elif a == c and b == d:
        print("Je to obdélník.")
    else:
        print("Je to nepravidelný čtyřúhelník.")


get_quadrangle_type(20,20,20,20)