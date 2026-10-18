import math
def quadratic(a,b,c):
    aaa = b**2 - 4*a*c
    if aaa < 0:
        return "No real roots"
    elif aaa == 0:
        return -b/(2*a)
    else:
        root1 = (-b + math.sqrt(aaa)) / (2*a)
        root2 = (-b - math.sqrt(aaa)) / (2*a)
        return root1, root2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
import math

# def quadratic(a, b, c):
#     if a == 0:
#         raise ValueError('a 不能为 0')
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         raise ValueError('No real roots')
#     if delta == 0:
#         x = -b / (2 * a)
#         return x, x
#     sqrt_delta = math.sqrt(delta)
#     denom = 2 * a
#     return (-b + sqrt_delta) / denom, (-b - sqrt_delta) / denom