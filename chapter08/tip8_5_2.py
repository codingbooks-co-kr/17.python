# ❶ 오류방지1 - list()로 키 리스트를 복사하여 순회
fruits = {"apple": 1000, "banana": 2500, "cherry": 5000}
for item in list(fruits.keys()): 		# 정상 동작
    if item.startswith('a'):		# 키가 "apple"이면
        del fruits[item]	  	# 해당 항목 삭제
print(fruits)

# ❷ 오류방지2 - 빈 딕셔너리 생성 후 'a'로 시작하지 않는 항목만 추가
fruits = {"apple": 1000, "banana": 2500, "cherry": 5000}
result = {}			# 새로운 빈 딕셔너리 생성
for item, price in fruits.items():	# 원본 딕셔너리의 각 항목을 순회
    if not item.startswith('a'):		# 'a'로 시작하지 않는 항목만 선택 (삭제 효과)
        result[item] = price		# 조건에 맞는 항목을 새 딕셔너리(result)에 추가
print(result)

# ❸ 오류방지3 - 딕셔너리 함축(8.7절)으로 새 딕셔너리 생성 후, 'a'로 시작하지 않는 항목만 추가
fruits = {"apple": 1000, "banana": 2500, "cherry": 5000}
result = {item: price for item, price in fruits.items() if not item.startswith('a')}
print(result)