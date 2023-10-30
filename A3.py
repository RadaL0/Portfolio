x = input().upper()
y = 0
q = ""
for i in x:
  if i.isalpha():
    if y<x.count(i):
      y = x.count(i)
      q = i
    elif y == x.count(i) and i not in q:
      q += i
print("".join(sorted(q)))
print(y)