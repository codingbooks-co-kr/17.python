# ❶ 기본 언패킹: 키만 할당됨
student = {"name": "민수", "age": 20}
key1, key2 = student	# 또는 key1, key2 = student.keys()
print(key1, key2)

# ❷ items() 언패킹: (키, 값) 튜플 쌍을 변수에 할당
student = {"name": "민수", "age": 20}
item1, item2 = student.items()
print(item1, item2)