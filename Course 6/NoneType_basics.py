# None 表示"什么都没有"

score = None  # 还没有成绩


if score == None:
    ## ==: 判断值是否相等，is是否是同个对象
    print("尚未评分")
else:
    print(f"成绩：{score}")

# 函数没有 return，默认返回 None
def say_hello():
    print("Hello")

result = say_hello()
print(result)        # None
print(type(result))  # <class 'NoneType'>
