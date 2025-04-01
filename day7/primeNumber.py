def check_prime_num(x):
    if x < 2:
        print(f"{x}은 소수가 아닙니다. 소수는 2 이상의 자연수입니다.")
        return False

    for i in range(2, x):
        if x % i == 0:
            print(f"{x}은 {i}로 나누어 떨어지므로 소수가 아닙니다.")
            return False

    print(f"{x}은 소수입니다.")
    return True
  
number = int(input("판별할 자연수를 입력하세요: "))
check_prime_num(number)
