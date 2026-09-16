# ❶ 3의 배수 필터링: 1부터 20까지의 숫자 중 3의 배수만 추출 후 (정수, "3배수") 쌍으로 딕셔너리 생성
result = {x: "3배수" for x in range(1, 21) if x % 3 == 0}
print(result)

# ❷ 특정 항목 제외: 기존 딕셔너리에서 키가 "apple"이 아닌 항목만 추출 후 딕셔너리 생성
fruits = {"apple": 2, "banana": 5, "kiwi": 3, "blueberry": 12}
result = {fruit: num for fruit, num in fruits.items() if fruit != "apple"}
print(result)

# ❸ 기준 점수 필터링: 기존 딕셔너리에서 점수가 80점 이상인 항목만 추출 후 딕셔너리 생성
scores = {"민수": 95, "지수": 66, "진우": 75, "소라": 82}
result = {name: score for name, score in scores.items() if score >= 80}
print(result)

# ❹ 단어 길이 필터링: 리스트에서 길이가 6 이상인 단어 요소만 추출 후 (단어, 문자수) 쌍으로 딕셔너리 생성
fruits = ["apple", "banana", "kiwi", "cherry", "blueberry"]
result = {fruit: len(fruit) for fruit in fruits if len(fruit) >= 6}
print(result)