# 声明
x = []
fruit = ["apple", "orange", "pineapple"]

# 读取
## 读取单个元素
print(fruit[0]) # apple
## 读取多个元素。语法：<list名>[a:b]，得到的是[a:b)（包括索引a，不包括索引b）
print(fruit[1:3]) # ['orange', 'pineapple']
## 遍历数组
for f in fruit:
  print(f, end=" ") # apple orange pineapple
print()


# 修改 
## 1 直接修改读取的元素
fruit[0] = "pear"
print(fruit) # ['pear', 'orange', 'pineapple']
## 也可以使用切片进行修改
m = [1, 2, 3, 4, 5, 6]
m[1:3] = ["x"] # [1, 'x', 4, 5, 6]
print(m)
## 2 利用list原生函数在末尾增加元素
m.append(7)
print(m) # [1, 'x', 4, 5, 6, 7]


# 查找
## 查询是否包含
print("pear" in fruit) # True
print("apple" in fruit) # False
## 查询list长度
print(len(fruit))

#删除
## 1 删除并取出
t = ['a', 'b', 'c']
x = t.pop(1)
print(t) # ['a', 'c']
print(x) # b

## 2 根据索引删除
t = ['a', 'b', 'c']
del t[1]
print(t) # ['a', 'c']
### 还可以一次删除多个
p = ['a', 'b', 'c', 'd', 'e']
del p[1:3]
print(p) # ['a', 'd', 'e']

## 3 根据内容删除
t = ['a', 'b', 'c']
t.remove('b')
print(t) # ['a', 'c']

# 排序
random = [1, 65, 0, 3, 25]
random.sort()
print(random) # [0, 1, 3, 25, 65]
## sort也可以可以传入一个函数，来自定义排序行为，举例：
words = ["apple", "pie", "a", "banana"]
words.sort(key=len)  # 按字符串长度排序
print(words)  # ['a', 'pie', 'apple', 'banana']

# 也可以用自定义函数实现降序排序
def reverse_value(x):
    return -x

numbers = [1, 65, 0, 3, 25]
numbers.sort(key=reverse_value) # -> [-1, -65, 0, -3, -25]
print(numbers)  # [65, 25, 3, 1, 0]

# 其他操作符: * ：把元素重复n遍
print(t * 2) # ['a', 'c', 'a', 'c']
# 其他操作符: + ：把两个list连接起来
j = ["Hi", "我是", "蔡徐坤"]
print(t + j)
# 其他操作符：针对number型list设计的便捷函数
nums = [3, 41, 12, 9, 74.5, 15]
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


