#默认情况下，dict迭代的是key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
#%%
#如果要迭代value，可以用for value in d.values()
d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)
#%%
#如果要同时迭代key和value，可以用for k, v in d.items()
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(key, value)
#%%
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable
isinstance('abc', Iterable) # str是否可迭代
#%%
from collections.abc import Iterable
isinstance([1,2,3], Iterable) # list是否可迭代
#%%
from collections.abc import Iterable
isinstance(123, Iterable) # 整数是否可迭代
#%%
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min_val = max_val = L[0]
    for x in L:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return (min_val, max_val)
print(findMinAndMax([7, 1, 3, 9, 5]))
#测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
# %%
