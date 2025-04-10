# 1)아아 :2000 2) 라때 : 2500
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
prices = [1500, 2500, 4000]
total_price = 0
amounts = [0, 0, 0]
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
    menu = input(menu_texts)
    if menu =="1":   #f는 f-string으로 문자열 안에서 변수, 함수 사용가능
        order_process(int(menu) -1)

    elif menu =="2":
        order_process(int(menu) - 1)

    elif menu == "3":
        order_process(int(menu) -1)

    elif menu == "4":
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")

print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")
print(f"총 주문 금액 : {total_price}원")