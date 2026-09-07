text = "Hello, world!"
# 这趴直接复制了示范里面统计词频的代码
d = dict()
for c in text:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1

# 接下来我要做的是把（词-次数）的对子调换顺序变成（次数-词）的对子
# 因为所有的排序或比较方法都是基于一个对子的第一个元素进行排序的
# 所以我要调换后对次数进行排序，排完了再重新把（次数-词）换回（词-次数）的对子

# 新建一个list叫做storage，用来存储调换顺序后的对子
storage = []
# unpacking语句，把每个元素都提出来，调换顺序构建新的tuple，然后
# 存入storage里面
for k, v in d.items():
    storage.append((v, k))
# 使用sorted()进行排序，把排序后返回的结果存入新list叫做sorted_list
sorted_list = sorted(storage, reverse=True)
# 上一行也可以替换为storage.sort(reverse=True)，但注意List.sort()是
# 不会返回数组的，而是再原数组里调换顺序。所以你需要继续使用storage完成接下来的步骤

# 新建一个空dictionary，用来存放排序完成后的词频统计表
sorted_dict = {}
# 遍历sorted_list中的对子，同样使用unpacking拆出每个元素，调换顺序后放进sorted_dict
for k, v in sorted_list:
    sorted_dict[v] = k
print(sorted_dict)
    

