# ❶ for문에서 enumerate()를 사용하지 않은 경우 (전통적 방식)
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# ❷ enumerate()로 객체 생성 후 리스트 변환
fruits = ["apple", "banana", "cherry"]
result = enumerate(fruits)
print(result)	# enumerate 객체
print(list(result))	# 객체→리스트 변환