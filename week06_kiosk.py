# 1)아아 :2000 2) 라때 : 2500
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
prices = [1500, 2500, 4000]
total_price = 0
amounts = [0, 0, 0]
#order_list =""
menu_texts = ""
for j in range(len(drinks)):
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원"
menu_texts = menu_texts + f"{len(drinks)+1} 주문종료 : "
while True:                              #배열 순서

    menu = input(menu_texts)
    if menu =="1":   #f는 f-string으로 문자열 안에서 변수, 함수 사용가능

        print(f"{drinks[0]}를 주문하셨습니다. 가격은 {prices[0]}원 입니다")
        total_price = total_price + prices[0]
        amounts[0] = amounts[0] + 1

    elif menu =="2":
        print(f"{drinks[1]}를 주문하셨습니다. 가격은 {prices[1]}원 입니다")
        total_price = total_price + prices[1]
        amounts[1] = amounts[1] + 1

    elif menu == "3":
        print(f"{drinks[2]}를 주문하셨습니다. 가격은 {prices[2]}원 입니다")
        total_price = total_price + prices[2]
        amounts[2] = amounts[2] + 1

    elif menu == "4":
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")

#print(order_list)
# print(f"{drinks[0]} {prices[0]}원 {amounts[0]}잔 {prices[0] * amounts[0]}원")
# print(f"{drinks[1]} {prices[1]}원 {amounts[1]}잔 {prices[1] * amounts[1]}원")
# print(f"{drinks[2]} {prices[2]}원 {amounts[2]}잔 {prices[2] * amounts[2]}원")
print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")
print(f"총 주문 금액 : {total_price}원")