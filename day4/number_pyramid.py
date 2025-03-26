s = ""
n = 1
for i in range(3):
  s += ' ' * (2 - i)
  for j in range (2 * i + 1):
    s += str(n)
    n += 1
  s += '\n'

print(s)
