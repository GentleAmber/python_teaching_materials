# 声明新dictionary
# 方式一（英汉词语对照表）
eng2ch = dict()
## 也可以在创建时就传入一个可遍历的序列，只要这个序列中的每个元素中还能找到一对键-值
## 可遍历的序列包括list, string, tuple，dictionary。
## 在这里我传入一个tuple A，这个tuple A里只有一个元素，
## 那就是另一个tuple B("dictionary", "字典")
# eng2ch = dict(("dictionary", "字典"),)
# print(eng2ch) # {'dictionary': '字典'}
## 你会发现可以创建成功，且自动把元素里的第一个值作为键，第二个值作为值。
## 但如果tuple B 有三个值，创建就会失败。

# eng2ch = dict((("dictionary", "字典", "搅局者"),)) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
# print(eng2ch)

# 方式二（计数表）
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}


# 写入元素
eng2ch["dictionary"] = "字典"
eng2ch["list"] = "列表"
eng2ch["orchard"] = "果园"

# 读取元素
print(eng2ch["dictionary"]) # 字典
## 检查元素是否存在，只能检查key是否存在
print("dictionary" in eng2ch) # true
print("字典" in eng2ch) # false

## 提取出所有的值，形成一个列表结构，但其种类并非列表
all_value = eng2ch.values()
print(all_value)
print(type(all_value))
# print(all_value[2])

### 如果想要用使用列表的方式来使用这些值，需要使用list()进行转换
### （类似于 str(2)）
value_list = list(all_value)
print(type(value_list))
print(value_list[2])

## 遍历，以计数表为例
for key in counts:
  print(key, counts[key])

# 修改元素
## 修改值：与list类似，使用索引选到值后进行修改
eng2ch["dictionary"] = "词典"
print(eng2ch["dictionary"])
## 修改键
### 方式一：使用新键继承旧键的值，然后删除旧键对应的【元素】
eng2ch["array"] = eng2ch["list"]
del eng2ch["list"]
print(eng2ch)
### 方式二：使用pop()方法取出旧键对应的【值】，赋给新键
eng2ch["vineyard"] = eng2ch.pop("orchard")
print(eng2ch)

# 与tuple的联系
## 我们已经知道.values()可以取出所有的值，同理，.keys()可以取出所有的键
## 当需要取出键值对的时候（一个完整的dictionary元素），我们使用items()
## 并且这个键值对的本质是一个tuple
print(eng2ch.items())
## 把dict_items转换为一个list
items_list = list(eng2ch.items()) 
print(type(items_list[0])) # <class 'tuple'>

# 利用tuple进行排序
## dictionary并无原生的排序方法。需要排序时，得借助tuple来实现
## sorted()方法是个原生方法，接收任意的可遍历序列（包括string），
## 排序后以list的形式输出
print(sorted("bdca")) # ['a', 'b', 'c', 'd']
items_sorted = sorted(eng2ch.items())
print(items_sorted) # [('array', '列表'), ('dictionary', '词典'), ('vineyard', '果园')]
print(type(items_sorted)) # list
## 注意此时items_sorted符合被传入dict构造dictionary的条件了，
## 所以我们直接调用dict()，传入items_sorted来构造新的dictionary
eng2ch_sorted = dict(items_sorted)
print(eng2ch_sorted)