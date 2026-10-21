#递归函数
#%%
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
#%%
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):/
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))
# > fact_iter(5, 1)
# => fact_iter(4, 5)
# => fact_iter(3, 20)
# => fact_iter(2, 60)
# => fact_iter(1, 120)
# => 120
#%%
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)   # ① 上面 n-1 个：从 a 借助 c 挪到 b
        print(a, '-->', c)     # ② 最大的那个：从 a 直接到 c
        move(n - 1, b, a, c)   # ③ 那 n-1 个：从 b 借助 a 挪到 c
move(3, 'A', 'B', 'C')
#%%
#斐波那契数列
def fib(n):
    if n <= 2:                 # 基线：前两项都是 1
        return 1
    return fib(n - 1) + fib(n - 2)   # 递推：前两项之和
print(fib(10))
for i in range(1, 11):
    print(fib(i))
#%%
#斐波那契数列（迭代）

def fib_iter(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
print(fib_iter(10))
for i in range(1, 11):
    print(fib_iter(i))
#%%
def fib(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
print(fib(10))
for i in range(1, 11):
    print(fib(i))  
#%%
# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。









