# str.endswith(suffix[, start[, end]])
# 检查字符串（或其切片）是否以suffix结束。也可以传入多个suffix组成的tuple
print(f"Title以le结尾: {sample.endswith('le')}")
print(f"Title以le或at结尾: {sample.endswith(('le', 'at'))}")
print(f"Title的第0-2位子字符串以it结尾: {sample.endswith('it', 0, 3)}")

# str.find(sub[, start[, end]])
# 找到子字符串首次在字符串中出现的索引
new_sample = (sample + " ") * 3
print("New sample: " + new_sample)
print(f"new_sample中首次出现“tle”的索引：{new_sample.find('tle')}")

# str.isalnum()
# alnum 是 alpha 和 number 的合并缩写。
# 用于判断字符串中的所有字符是否都是字母数字类且至少有一个字符
sample2 = ""
print(f"\"\"符合字母数字类：{sample2.isalnum()}")
sample2 = "f2"
print(f"\"f2\"符合字母数字类：{sample2.isalnum()}")
sample2 = "鲧"
print(f"\"鲧\"符合字母数字类：{sample2.isalnum()}")

# 其他方法略