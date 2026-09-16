# ❹ 문자열 리스트에 map() 함수를 적용한 예
names = ["kim", "lee", "park"]

# 리스트의 문자열 요소를 대문자로 변환 (str.upper() 메서드 사용)
result = map(str.upper, names)
print(list(result))

# 리스트의 문자열 요소를 각 요소의 길이로 변환 (len() 함수 사용)
result = map(len, names) 
print(list(result))