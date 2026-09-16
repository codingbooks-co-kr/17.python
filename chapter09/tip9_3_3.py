# ❸ 문자열 리스트에 리스트 함축을 적용한 예
words = ["apple", "banana", "kiwi", "watermelon"]

# 문자열 리스트에서 'e'가 포함된 문자열만 필터링
result = [x for x in words if 'e' in x]
print(result)

# 문자열 리스트의 요소 중 길이가 6 이상인 문자열만 필터링
result = [x for x in words if len(x) >= 6]
print(result)