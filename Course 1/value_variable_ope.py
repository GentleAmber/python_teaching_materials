# 值和类型 -----------------------------
print("Hello world.")

print(type("Hello world."))
print(type(1)) # int
print(type(1.4)) # float
print(type(True)) # bool (boolean)

# 变量 -----------------------------
x = 3
print(type(x))
x = "abc"
print(type(x))

# 运算符 -----------------------------
# 数值运算
# + - * / % **
print("3的立方：" + str(3**3))
print("8除以4.1：" + str(8 / 4.1))
print("8整除4.1：" + str(8 // 4.1))
print("8除以4.1的余数：" + str(8 % 4.1))

# 字符运算
first = "First"
second = "Second"
print(first + " " + second) # "+"作为连接符
repeat = 2
print(first * repeat) # "*"作为重复次数，重复次数必须是int类型
