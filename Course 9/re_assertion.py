import re

# assertion 断言
# (?=…) 前视断言
# 比如， Isaac (?=Asimov) 将会匹配 'Isaac '，仅当其后紧跟 'Asimov'。

pattern = r"\w+(?= fox)"

text = "a quick fox"
print(re.search(pattern, text))
print(re.search(pattern, text).group())