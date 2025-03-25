# 1.이중 while문
# 2. 단 홀 x 홀
# 3. 단 짝 x 짝
# 코딩 룰 체크

# 9번 반복하기
i = 1
print("홀수")
while i <= 9:
  j = 1
  while j <= 9:
    if  i % 2 == 1 and j % 2 == 1:
      print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
    j += 1
  i += 1

print("\n짝수")
i = 2
while i <= 9:
  j = 1
  while j <= 9:
    if  i % 2 == 0 and j % 2 == 0 :
      print(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
    j += 1
  i += 2
