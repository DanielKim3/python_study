s = ""
l = 0
try:
  n = float (input("행을 입력하세요 : "))
  m = float (input("열을 입력하세요 : "))
  if (n % 1 != 0) | (m % 1 != 0 ) | (n <= 0) | ( m <= 0):
    print("에러 발생")
  else:
    for i in range(int(n)):
      for j in range(1, int(m) + 1):
        s += str(j + l) + " "
      s += '\n'
      l += 1
    print(s)
except ValueError:
  print("에러 발생")

