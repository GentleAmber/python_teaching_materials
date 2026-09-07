def add_score(name, score, record=[]):
    # 把 (姓名, 分数) 加入记录列表，并返回该列表
    record.append((name, score))
    return record


def show_class(class_name, students):
    print(f"班级 {class_name} 的成绩单：")
    for name, score in students:
        print(f"  {name}: {score}")



class1 = add_score("小明", 90)
class1 = add_score("小红", 85, class1)
show_class("一班", class1)

# 预期：二班是全新的成绩单，只有小刚一个人
class2 = add_score("小刚", 78)
show_class("二班", class2)

print(class1 is class2)












## 出现该情况的原因：对于传入函数的默认参数，python规定：Default values are computed once, then re-used.
## 这对类似于 def defaultAddFive(num, add=5) 这样的函数来说，不管调用多少次，都引用同一个5。是节省内存的
## 但当默认参数是可变数据类型时，就会出现此处展示的表现问题
