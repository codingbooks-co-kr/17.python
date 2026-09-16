# ❶ 제너레이터 표현식으로 (제너레이터/이터레이터) 객체 생성
my_gen = (x for x in range(1, 4))	# 제너레이터 표현식
for num in my_gen:
    print(num)

# ❷ next()를 사용해 값을 하나씩 꺼내기 (현재 값 1개만 메모리에 유지)
my_gen = (x for x in range(1, 4))	# 제너레이터 표현식
print(next(my_gen))		# next() 함수로 값을 하나씩 가져옴
print(next(my_gen))		# next() 함수로 값을 하나씩 가져옴
print(next(my_gen))		# next() 함수로 값을 하나씩 가져옴

# ❸ tuple()을 사용해 튜플로 변환 후 한꺼번에 담기 (모든 값을 메모리에 저장)
result = tuple(x for x in range(1, 4))
print(result)