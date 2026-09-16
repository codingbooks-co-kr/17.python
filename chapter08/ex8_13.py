# ❶ 숫자와 제곱수 매칭: 1부터 5까지의 정수를 키로, 그 제곱을 값으로 하는 새 딕셔너리 생성
result = {x: x*x for x in range(1, 6)}
print(result)

# ❷ 키(Key)만 변화: 기존 딕셔너리의 키를 대문자로 변환 후 새 딕셔너리 생성
info = {"name": "민수", "age": 20, "city": "서울"}
result = {key.upper(): value for key, value in info.items()}
print(result)

# ❸ 값(Value)만 변화: 기존 딕셔너리의 값만 두 배로 변환 후 새 딕셔너리 생성
fruits = {"apple": 2, "banana": 5, "kiwi": 3, "blueberry": 12}
result = {fruit: num * 2 for fruit, num in fruits.items()}
print(result)

# ❹ 글자와 글자 수 매칭: 리스트의 문자열 요소를 키로, 각 문자열의 길이를 값으로 하는 새 딕셔너리 생성
fruits = ["apple", "banana", "kiwi", "blueberry"]
result = {fruit: len(fruit) for fruit in fruits}
print(result)