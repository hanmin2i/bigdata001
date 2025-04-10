def is_prime(number : int) -> bool:
    """
     number:int 입력값은 정수형 반환값은 bool
    :param number:
    :return: True if it is prime number else False
    """
    is_prime = True

    if number >= 2:
       for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
            #print(i, end=" ")

    else:
        return False
    return True

n1 = int(input())
n2 = int(input())

if n1> n2:
    n1, n2 = n2,n1 # (n1,n2)가있으면 n1에 n2값을 넣어주고 n2에 n1값을 넣어주는 것 

for i in range(n1, n2+1): #숫자를 n1 부터 n2까지 돌린후 true면 출력
    if is_prime(i):
        print(i, end=' ')
# number = int(input())
# if is_prime:
#     print(f"{number}는 소수입니다")
# else:
#     print(f"{number}는 소수가 아닙니다")