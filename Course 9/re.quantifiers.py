import re

passwords = ["abc12", "abc123", "abc1234", "abc12345678"]
for p in passwords:
    if re.fullmatch(r'\w{6,8}', p): # 等同于re.match(r'^\w{6,8}$', p)
        print(f"✓ {p}")
    else:
        print(f"✗ {p}")

# {m,n} 是尽量取多的一个匹配
pattern = 'a{4,}b'
pattern2 = 'a{4,}?b'
texts = ["ab","aaaab","aaaaaaaab"]
for text in texts:
    matched = re.search(pattern, text)
    if (matched):
        print(f"✓ {matched.group()}")
    else:
        print(f"✗ {text}")

for text in texts:
  matched2 = re.search(pattern2, text)
  if (matched2):
      print(f"✓ {matched2.group()}")
  else:
      print(f"✗ {text}")