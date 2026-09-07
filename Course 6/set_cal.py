# Set的数学运算
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

## 1. 并集（union）：合并两个set，去重
union_result = set_a.union(set_b)
print(f"并集: {union_result}")  # {1, 2, 3, 4, 5, 6, 7, 8}
## 也可以使用|运算符
union_result2 = set_a | set_b
print(f"并集（使用|）: {union_result2}")  # {1, 2, 3, 4, 5, 6, 7, 8}

## 2. 交集（intersection）：找出两个set中都有的元素
intersection_result = set_a.intersection(set_b)
print(f"交集: {intersection_result}")  # {4, 5}
## 也可以使用&运算符

## 3. 差集（difference）：找出在set_a中但不在set_b中的元素
difference_result = set_a.difference(set_b)
print(f"差集 (set_a - set_b): {difference_result}")  # {1, 2, 3}
## 也可以使用-运算符

## 4. 对称差（symmetric_difference）：把两个集合交集的部分去除后合并
sym_diff = set_a.symmetric_difference(set_b)
print(f"对称差: {sym_diff}")  # {1, 2, 3, 6, 7, 8}
## 也可以使用^运算符