# ❶ 숫자의 나열(기본형): 1∼10까지의 숫자로 이루어진 리스트 생성
result = [i for i in range(1, 11)]
print(result)

# ❷ 산술연산(제곱하기): 1∼5까지의 숫자를 제곱한 리스트 생성
result = [i * i for i in range(1, 6)]
print(result)

# ❸ 메서드 활용(대문자 변환): 문자열 리스트를 대문자로 변환
words = ["python", "java", "c++", "c#"]
result = [word.upper() for word in words]
print(result)

# ❹ 인덱싱(첫글자 추출): 문자열 리스트에서 각 문자열의 첫 글자 추출
fruits = ["apple", "banana", "cherry", "blueberry"]
result = [fruit[0] for fruit in fruits]
print(result)

# ❺ 토큰화와 가공(문장처리): 모든 단어를 대문자로 변환
words = "Hello Python Coding"
result = [word.upper() for word in words.split()]
print(result)