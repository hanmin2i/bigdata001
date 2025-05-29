#open api : wttr.in (weather info)
#다시 재시작 할때 이미 db가 돌아가고 있는중이니 db browser에서 diconnect로 연결을 끊어주고 다시 실행

import kiosk as kk


if __name__ == "__main__":
    kk.run()
    kk.print_receipt()
    kk.print_ticket_number()