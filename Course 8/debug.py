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



