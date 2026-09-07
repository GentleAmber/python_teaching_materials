import re

m = re.search(r'(\d+)-(\d+)', 'tel: 138-1234')
print(m)
print(m.group(1), m.group(2))   # 138 1234

m = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})', '2024-06')
print(m.group('year'), m.group('month'))  # 2024 06

m = re.search(r'(\w+) \1', 'hello hello world')
print(m.group())

m = re.search(r'(?P<greeting>\w+) (?P=greeting)', 'hello hello world')
print(m.group())