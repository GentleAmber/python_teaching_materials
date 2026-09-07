# Python版本的 for(int i = 0; i <= 2; i++) {...}
for n in range(3): 
  print(n, end=" ")

print()

# Python的for的哲学：经过一个可遍历体中的每一个元素。
# 所以你可以用它来遍历字符，list，tuple，dictionary（后面介绍），
# 文本文件(.TXT)的每一行，等等
for letter in "HELLO":
  print(letter, end=" ")

print()

fruit = ["apple", "pear", "peach"] #list
for f in fruit:
  print(f, end=", ")