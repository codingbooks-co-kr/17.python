# ❷ 데이터 업데이트: 과일 바구니의 과일 개수 세기

basket = {"사과": 5, "바나나": 2}
fruit = input("과일명: ")	# 과일명 입력

if fruit in basket:
    basket[fruit] += 1	# 이미 있다면 개수를 1 증가
    print(f"{fruit}의 개수 증가!")
else:
    basket[fruit] = 1	# 없다면 1개로 새로 등록
    print(f"{fruit}을(를) 새로 등록!")

print(f"최종 바구니: {basket}")