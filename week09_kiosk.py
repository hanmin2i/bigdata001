
import kiosk as kk
# crtl + r

# 실제론 영향을 안받음 타입 힌트 -> 리턴값

while True:
    try:

        menu = int(input(kk.display_menu()))
        if len(kk.drinks) >= menu >= 1:
            kk.order_process(menu - 1)

        elif menu == len(kk.drinks) + 1:
            print(" 주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
    except ValueError:
        print("숫자를 입력해주십쇼")
kk.print_receipt()
