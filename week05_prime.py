def is_prime(number : int) -> bool:
    """

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
    n1, n2 = n2,n1

for i in range(n1, n2+1):
    if is_prime(i):
        print(i, end=' ')
# number = int(input())
# if is_prime:
#     print(f"{number}는 소수입니다")
# else:
#     print(f"{number}는 소수가 아닙니다")