import re

pattern = r'^\w+@\w+\.[a-zA-Z.]+[a-zA-Z]$' 

# r 前缀使字面值成为原始字符串字面值
# ^匹配字符串开头
# $匹配字符串结尾
# \w 匹配非符号的字符（字母、数字、中文）
# + 表示匹配1次或以上次数
# \. 转义复号表示字面意义的.，否则被作为特殊符号的含义处理
# []集合中的所有元素都可匹配，哪怕是.这样的特殊符号也可以直接写
emails = ["user@example.com", "bad-email", 'bad-email2@@jck.com', "hello@world.org", "jkca@email.co.uk", "skjf321@163.com"]
for email in emails:
  if re.match(pattern, email):
    print(f"✓ {email}")
  else:
    print(f"✗ {email}")