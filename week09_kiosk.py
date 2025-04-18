import kiosk


# 실제론 영향을 안받음 타입 힌트 -> 리턴값

while True:
    try:

        menu = int(input(kiosk.display_menu()))
        if len(kiosk.drinks) >= menu >= 1:
            kiosk.order_process(menu - 1)

        elif menu == len(kiosk.drinks) + 1:
            print(" 주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
    except ValueError:
        print("숫자를 입력해주십쇼")
kiosk.print_receipt()
