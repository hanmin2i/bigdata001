drinks = ["아이스 아메리카노","카페라떼","수박주스","딸기주스","콜드블루","아인슈페너"]
prices = [1500, 2500, 4000, 4500,2000,3500]
total_price = 0
amounts = [0] * len(drinks)

                   #실제론 영향을 안받음 타입 힌트 -> 리턴값
def order_process(idx : int) -> None:
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3) 수량 업데이트
    idx : 고객이 선택한 메뉴 -1 (인덱스, 정수)
    :return:없음
    """
    global total_price #global- 전역변수
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

def display_menu() -> str:
    '''
    음료선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열
    '''
    print("="*30)
    menu_texts = ' '.join([f"{j + 1}){drinks[j]} {prices[j]}원\n" for j in range(len(drinks))])
    menu_texts = menu_texts + f" {len(drinks) + 1})주문종료 : "
    return menu_texts

def print_receipt() -> None:
    '''
    영수증 출력 기능
    :return: 없음
    '''
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")
    print(f"총 주문 금액 : {total_price}원")



while True:    # 무한 루프
    try:
       
        menu = int(input(display_menu()))  # display함수실행 -> input 문자열 받음 -> int형으로 변환
        if len(drinks) >=menu >=1:
            order_process(menu-1)

        elif menu == len(drinks) + 1 :
            print(" 주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
    except ValueError:
        print("숫자를 입력해주십쇼")
print_receipt()
