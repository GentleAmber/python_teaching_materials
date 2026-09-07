text = "Hello, world!"

d = dict()
for c in text:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)

# loop1:
# d["H"] = 1
# d["e"] = 1
# d["l"] = 2