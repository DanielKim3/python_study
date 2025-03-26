while True:
  try:
    coin = float(input('동전을 넣으세요.'))    
  except ValueError:
    print("정수가 아닙니다")
    continue

  if coin <= 0:
    print("동전을 다시 넣어주세요")
    continue

  elif coin % 10 <= 9 and coin % 10 != 0:
    print("{}원은 취급하지 않습니다".format(coin))
    continue

  while((coin > 0) & (coin % 1 == 0)):
    print("====================================================================================")
    print('음료목록 1.오렌지주스(100원), 2.커피(200원), 3.콜라(300원) 9. 동전반환, 11.동전 넣기')
    print("====================================================================================")

    print("현재 금액 {} 원\n".format(int(coin)))
    drink = int(input('메뉴를 고르세요 : '))

    if drink == 1:
      #오렌지주스 100원
      if coin >= 100:
        remain = coin - 100
        print('\n오렌지주스가 곧 제공됩니다.')
        print('거스름돈은 {} 원 입니다.\n'.format(int(remain)))
        coin = remain
        print('현재금액 {} 원\n'.format(int(remain)))
      else:
        print('잔액이 부족합니다.')
        need = 100 - coin
        print('필요금액 {} 원\n'.format(int(need)))

    elif drink == 2:
      #커피 200원
      if coin >= 200:
        remain = coin - 200
        print('\n오렌지주스가 곧 제공됩니다.')
        print('거스름돈은 {} 원 입니다.\n'.format(int(remain)))
        coin = remain
        print('현재금액 {} 원\n'.format(int(remain)))
      else:
        print('잔액이 부족합니다.')
        need = 200 - coin
        print('필요금액 {} 원\n'.format(int(need)))

    elif drink == 3:
      #콜라 300원
      if coin >= 300:
        remain = coin - 300
        print('\n콜라가 곧 제공됩니다.')
        print('거스름돈은 {} 원 입니다.\n'.format(int(remain)))
        coin = remain
        print('현재금액 {} 원\n'.format(int(remain)))
      else:
        print('잔액이 부족합니다.')
        need = 300 - coin
        print('필요금액 {} 원\n'.format(int(need)))

    elif drink == 9:
      if coin != 0 :
        print('반환금액 {} 원 입니다.\n'.format(int(coin)))
        coin = 0
        print('현재금액 {} 원\n'.format(int(coin)))
      else:
        print("반환할 금액이 없습니다.")
        print("동전을 넣으세요.")

    elif drink == 11:
      add = float(input('추가 동전을 넣으세요: '))
      if add % 10 <= 9 and add % 10 != 0:
        print("{}원은 취급하지 않습니다".format(add))
        print("현재 금액 {} 원".format(int(coin)))
        continue

      coin += add
      print("현재 금액 {}원".format(int(coin)))

    else:
      #없는 번호
      print('없는 메뉴입니다. 다시 입력해 주세요.')
