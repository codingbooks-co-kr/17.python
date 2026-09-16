# ❹ 문자열 리스트에 리스트 함축을 적용한 예
names = ["kim", "lee", "park"]

# 리스트의 문자열 요소를 대문자로 변환 
result = [x.upper() for x in names]
print(result)

# 리스트의 문자열 요소를 각 요소의 길이로 변환 
result = [len(x) for x in names]
print(result)