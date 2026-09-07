# x = [1, 3, 4, 6, 7]
# y = x
# x.append(1)
# print(y)

# print(id(x))
# print(id(y))

# a = 3
# b = a
# a = 5
# print(id(a))
# print(id(b))

# class Dog:

#   def __init__(self, name):
#     self.name = name

#   def bark(self): # 改掉参数名也一样成立
#     print(f"Woof, {self.name}")

#   @classmethod 
#   def eat(cls):
#     print("eat")
    
# ivy = Dog("Ivy")
# print(type(ivy))

text = "id__no__en__ci__fw__sd"
for a, b in text:
  print((a, b))