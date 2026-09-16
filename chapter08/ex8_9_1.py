fruits = {"apple": 1000, "kiwi": 2500, "cherry": 5000}

# ❶ 모든 키:값 쌍 순회: 항목 중 모든 키를 대문자로 변환, 출력
for item, price in fruits.items():
    new_item = item.upper() 		# 키변환: 소문자→대문자
    print(f"{new_item}: {price}원")

# ❷ 모든 키:값 쌍 순회: 항목 중 모든 가격을 10% 인상 후 출력
for item, price in fruits.items():
    new_price = price * 1.1 		# 값변환: 10% 인상
    print(f"{item}: {new_price:.1f}원")

# ❸ 모든 키:값 쌍 순회: 과일 리스트에 포함되면 값 누적
total = 0				# 누적할 변수 초기화
for item, price in fruits.items():
    if item in ["apple", "kiwi"]:	# 리스트 포함 여부 확인
        total += price		# total 누적
print(f"구매할 과일 총액: {total}원")

# ❹ 모든 키:값 쌍 순회: 3000원 이상인 과일과 가격 출력
for item, price in fruits.items():
    if price >= 3000:
        print(f"{item}: {price}원")

# ❺ 모든 키:값 쌍 순회: 가격을 두 분류로 출력
for item, price in fruits.items():
    if price >= 3000:
        print(f"{item}: {price}원으로 비싸다.")
    else:
        print(f"{item}: {price}원으로 싸다.")