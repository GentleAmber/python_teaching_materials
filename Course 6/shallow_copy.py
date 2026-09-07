# list的复制(shallow copy)
original_list = [[1, 2], 3, 4]
copied_list = original_list.copy() 
## 修改副本不会影响原set
print(copied_list)
# original_list[0] = [1, 2, 5]
print(id(original_list[0]))
print(id(copied_list[0]))

original_list[0].append(5)

print(original_list)
print(copied_list)

