# 스마트홈 기기 제어

light1 = input("전등1 켜짐?(예/아니오): ")
light2 = input("전등2 켜짐?(예/아니오): ")
air_con = input("에어컨 켜짐?(예/아니오): ")
gas = input("가스 잠김?(예/아니오): ")

# 각 기기의 상태를 독립적으로 검사
if light1 == "예":
    print("전등1 켜짐!")
if light2 == "예":
    print("전등2 켜짐!")
if air_con == "예":
    print("에어컨 켜짐!")
if gas == "예":
    print("가스 잠김!")