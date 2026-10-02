# print("你好，Git")
# print("欢迎使用Git")
# classmate = ['TOM', 'JACK', 'LILY']
# print(classmate)
# print(len(classmate))
# print(classmate[0])
# print(classmate[-1])
# score = 'B'
score = input("请输入成绩等级（A/B/C）：")
if score == 'A':
    print("优秀")
elif score == 'B':
    print("良好")
elif score == 'C':
    print("及格")
else:
    print("未知分数")

# 遍历班级名单列表，逐个打印每位同学的姓名（格式：同学：TOM）
classmates = ['TOM', 'JACK', 'LILY']
for name in classmates:
    print("同学：" + name)
