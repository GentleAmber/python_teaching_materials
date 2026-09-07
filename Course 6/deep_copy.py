import copy

original_list = [[1, 2], 3, 4]
deep_copied_list = copy.deepcopy(original_list)

original_list[0].append(5) 
print(original_list)
print(deep_copied_list)
