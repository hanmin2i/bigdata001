drinks = ["아이스 아메리카노", "카페라떼", "수박주스" , "딸기주스"]    #len은 리스트 안에 들어있는 원소 갯수
prices = [1500, 2500, 4000, 4500]
total_price = 0
amounts = list()
for _ in range(len(drinks)):
    amounts.append(0)      #append 리스트안에 데이터 추가
menu_texts = ""

def order_process(idx):
    """
    주문 처리 함수 1) 주문 디스플레이 2)총 주문 금액 누산 3) 수량 업데이트  
    :return:없음
    """
    global total_price #global- 전역변수
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1

for j in range(len(drinks)):
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원"
menu_texts = menu_texts + f"{len(drinks)+1} 주문종료 : "

while True:
    menu = int(input(menu_texts))
    if len(drinks) >=menu >=1:                                #f는 f-string으로 문자열 안에서 변수, 함수 사용가능
        order_process(menu-1)

    elif menu == len(drinks) + 1 :
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")

print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")
print(f"총 주문 금액 : {total_price}원")