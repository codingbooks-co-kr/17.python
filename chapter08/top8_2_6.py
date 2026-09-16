# ❶ 0~10의 숫자 중 짝수만 추출 후 제곱 (순서없음)
result = {x**2 for x in range(11) if x % 2 == 0}
print(result)

# ❷ 두 리스트의 공통 요소 추출
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = {x for x in a if x in b}
print(result)

# ❸ 단어 길이가 4 이상인 단어만 추출 (중복제거/순서없음)
words = {"apple", "banana", "cat", "dog", "elephant"}
result = {word for word in words if len(word) >= 4}
print(result)

# ❹ 문자열에서 알파벳 추출→소문자 변환 (중복제거/순서없음)
words = "Hello, Python! 123"
result = {c.lower() for c in words if c.isalpha()}
print(result)

# ❺ 문자열에서 모음 추출 (중복제거/순서없음)
words = "Hello, Python! 123"
result = {c for c in words if c.lower() in "aeiou"}
print(result)