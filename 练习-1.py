#match的用法
# age = int(input('Please input your age: '))

# match age:

#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# 难点3：case ['gcc', file1, *files]: —— 变长匹配
# 这是最“魔法”的地方。

# 'gcc'：包裹第一个东西必须是“gcc”。

# file1：把第二个东西抓出来，起个名字叫 file1。
# 比如 args = ['gcc', 'hello.c', 'world.c']，那么 file1 就等于 'hello.c'。

# *files：把剩下所有的东西（从第三个开始）装进一个叫 files 的小篮子。
# 上面例子中，files = ['world.c']。
# 如果只有两个东西（['gcc', 'hello.c']），files 就是空篮子 []。

# 通俗理解：
# “gcc”打头，第二个文件我单拎出来叫 file1（可能用于特殊处理），剩下的不管有多少个，全部放一堆叫 files。
# * 就像吸尘器，把剩下的全部吸进来。```









