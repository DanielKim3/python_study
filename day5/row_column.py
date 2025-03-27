s = ""
l = 0
try:
  n = float (input("행을 입력하세요 : "))
  m = float (input("열을 입력하세요: "))
  for i in range(int(n)):
    for j in range(1, int(m) + 1):
      s += str(j + l) + " "
    s += '\n'
    l += 1
  print(s)
except ValueError:
  print("에러 발생")
