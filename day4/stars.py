s = "*"
try:
  n = int(input())
  if n < 0:
    print("음수는 사용할 수 없습니다")
  else:
    for i in range(1, n + 1):
     print(i * s)
except ValueError:
  print("에러 발생")
  
