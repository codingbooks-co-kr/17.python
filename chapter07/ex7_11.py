# 리스트 관련 다양한 메서드

fruits = ["사과", "딸기", "수박", "포도"]

# count(): 지정한 요소가 출현하는 횟수 반환
result = fruits.count("사과")
print(result)

# index(): "수박"이 처음 출현하는 인덱스 반환
result = fruits.index("수박")
print(result)

# append(): 리스트 끝에 새로운 요소 추가
fruits.append("귤")
print(fruits)

# insert(): 리스트의 특정 요소에 새로운 요소 삽입
fruits.insert(1, "배")
print(fruits)

# remove(): 리스트에서 첫 번째로 출현하는 특정 요소 제거
fruits.remove("딸기")
print(fruits)

# pop(): 특정 위치의 요소를 꺼내서 반환
result = fruits.pop(1)
print(result, fruits)

# pop(): (인덱스 생략 시) 마지막 요소를 꺼내서 반환
result = fruits.pop()
print(result, fruits)

# reverse(): 리스트의 요소 순서 뒤집기
fruits.reverse()
print(fruits)

# join(): 요소들 사이 공백문자 삽입 후 하나의 문자열로 결합
result = " ".join(fruits)
print(result)

# clear(): 리스트의 모든 요소 제거 → 빈 리스트 생성
fruits.clear()
print(fruits)