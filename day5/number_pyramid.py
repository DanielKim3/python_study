s = ""
p = 1
n = int(input('숫자를 입력해주세요 : '))
if(n <= 9 and n > 0):
  for i in range(1):
      for j in range(1, n+1):
        if j == 1:
          s += ' ' * (2)
          s += str(p)
          p += 1
          s += '\n'
        elif j == 2:
          s += ' ' * (1)
          for _ in range(3):
            if p > n:
                break
            s += str(p)
            p += 1
          s += '\n'
        else:
          if p > n:
            break
          s += str(p)
          p += 1
  print(s)
else:
  print("1이상 10 미만으로 작성하시오.")

