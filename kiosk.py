drinks = ["아이스 아메리카노", "카페라떼", "수박주스", "딸기주스"]
prices = [1500, 2500, 4000, 4500]
total_price = 0
amounts = [0] * len(drinks)

def order_process(idx: int) -> None:
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3) 수량 업데이트
    idx : 고객이 선택한 메뉴 -1 (인덱스, 정수)
    :return:없음
    """
    global total_price  # global- 전역변수
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


def display_menu() -> str:
    '''
    음료선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열
    '''
    print("=" * 30)
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

def test()-> None:
    '''
    
    :return:
    '''
    return