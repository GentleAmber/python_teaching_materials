# 声明新set（集合）
# 方式一：使用花括号{}和逗号分隔的元素
fruits = {'apple', 'banana', 'orange', 'apple'}
## 注意：set会自动移除重复的元素
print(fruits)  # {'apple', 'banana', 'orange'}

# 方式二：使用set()构造函数传入一个可遍历序列
numbers = set([1, 2, 3, 3, 4, 5, 5, 5])
## list中有重复元素，但转换为set后重复被移除
print(numbers)  # {1, 2, 3, 4, 5}
## 注意str同样是一个可遍历序列
chars = set("hello")
print(chars)  # {'h', 'e', 'l', 'o'}

# 方式三：创建空set（注意：不能用{}，因为{}代表空dictionary）
empty_set = set()
print(type(empty_set))  # <class 'set'>
print(empty_set)  # set()


# 添加元素
## 使用add()方法添加单个元素
fruits.add('grape')
print(fruits)  # {'apple', 'banana', 'orange', 'grape'}

## 如果添加已存在的元素，set不会改变（不会报错）
fruits.add('apple')
print(fruits)  # 与之前相同，没有添加重复元素

## 使用update()方法添加多个元素（来自list、tuple或另一个set）
fruits.update(['mango', 'pineapple', 'banana'])
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'mango', 'pineapple'}


# 删除元素
## 方式一：使用remove()删除指定元素，如果元素不存在会报错
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}
numbers.remove(3)
print(numbers)  # {1, 2, 4, 5, 6}
numbers.remove(10)  # KeyError: 10（报错，因为10不存在）

## 方式二：使用discard()删除指定元素，如果元素不存在不会报错
numbers.discard(1)
print(numbers)  # {2, 4, 5, 6}
numbers.discard(100)
print(numbers)  # {2, 4, 5, 6}（100不存在，但没有报错）

## 方式三：使用pop()删除并返回任意一个元素
removed_item = numbers.pop()
print(f"被删除的元素: {removed_item}")
print(numbers)
## push pop: 后进先出

## 方式四：使用clear()清空整个set
temp_set = {1, 2, 3}
temp_set.clear()
print(temp_set)  # set()

# 检查成员关系
colors = {'red', 'green', 'blue'}
print('yellow' in colors)  # False
print('yellow' not in colors)  # True


# 遍历set
## set中的元素没有特定的顺序，所以遍历顺序可能不同
animals = {'dog', 'cat', 'bird', 'fish'}
for animal in animals:
    print(animal)

# Set的包含关系
set_x = {1, 2, 3}
set_y = {1, 2}

## 检查一个set是否是另一个set的子集
print(set_y <= set_x)  # True

## 检查一个set是否是另一个set的超集
print(set_x >= set_y)  # True