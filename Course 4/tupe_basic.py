x = 1, 2
print(type(x)) # class 'tuple'

# 按照惯例，会加上前后括号表示这是一个tuple
x = (1, 2)
print(type(x)) # class 'tuple'
# 单一元素tuple必须带逗号
x = (1,)
y = (1)
print(type(x)) # class 'tuple'
print(type(y)) # class 'int'

# 查找
## 仍然可以使用 <tuple名>[a:b]的方式切片，或使用索引提取
x = (1, 2)
print(x[0]) # 1
print(x[0:2]) # (1, 2)
for a in x:
  print(a, end=" ") # 1 2
print()
print(1 in x) # True

# 无法删改tuple。此类操作会报错：
x[0] = 3 # TypeError: 'tuple' object does not support item assignment

