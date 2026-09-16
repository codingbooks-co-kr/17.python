fruits = {"apple": 1000, "kiwi": 2500, "cherry": 5000}

# ❻ 키 확인-1: 키가 "apple"이면 해당 키의 값 출력
for item in fruits:
    if item == "apple": 		# 키가 "apple"인지 확인
        print(f"{item}: {fruits[item]}원")

# ❼ 키 확인-2: 'a'로 시작하는 키의 값 출력
for item in fruits.keys():  		# 딕셔너리의 모든 키 순회
    if item.startswith("a"):  		# 키가 "a"로 시작하는가?
        print(f"{item}: {fruits[item]}원")

# ❽ 키 확인-3: 'a'로 시작하는 키의 항목 삭제 → [꿀팁8.4] 참조
for item in list(fruits.keys()): 		# 딕셔너리의 모든 키 순회
    if item.startswith("a"):  		# 키가 "a"로 시작하는가?
        del fruits[item]		# "apple" 항목 삭제
print(fruits)