def is_prime(number): #is_prime 함수 정의
    """
    def 함수이름(매게 변수) 함수를 정의할때 사용
      실행 코드 
      return 반환값
    :param number: param은 함수의 인자 설명 number는 정수
    :return: True if it is prime number else False return은 반환값 설명
    """
    pass
    is_prime = True

    if number >= 2:
       for i in range(2, int(number**0.5) + 1): #i는 2부터 시작 number에 루트를 씌운값 까지 실행후 i+1
            if number % i == 0:
                return False
            #print(i, end=" ")

    else:
        return False
    return True
number = int(input())
if is_prime(number):
    print(f"{number}는 소수입니다")
else:
    print(f"{number}는 소수가 아닙니다")