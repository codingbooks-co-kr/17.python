# ❸ for문에서 enumerate()를 사용하는 경우 (인덱스 0부터 시작)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ❹ for문에서 enumerate()를 사용하는 경우 (인덱스 1부터 시작)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# ❺ 숫자 리스트에서 80점 이상의 점수만 인덱스와 함께 표시
scores = [85, 90, 78, 65, 95]
for index, score in enumerate(scores):
    if score >= 80:
        print(index, score)

# ❻ 문자열의 각 문자에 인덱스 표시
word = "abc"
for index, char in enumerate(word):
    print(index, char)

# ❼ 딕셔너리의 키와 값을 인덱스와 함께 표시
scores = {"민수": 90, "지수": 85, "진우": 92}
for index, (name, score) in enumerate(scores.items(), start=1):
    print(index, name, score)