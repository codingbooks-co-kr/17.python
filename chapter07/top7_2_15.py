# 리스트 함축과 제너레이터 표현식 비교

# ❶ 리스트 함축: 대괄호 []로 명시, 반환 결과는 리스트 객체
result = [x for x in range(1, 6)]	# 리스트 함축
print(result)			# 실행결과: [1, 2, 3, 4, 5]

# ❷ 제너레이터 표현식은 소괄호 ()로 명시, 반환 결과는 튜플이 아니라 제너레이터 객체
result = (x for x in range(1, 6))	# 제너레이터 표현식
print(result)	 # 실행결과: <generator object <genexpr> at 0x000001EAAE925F00>

# ❸ next()를 사용해 제너레이터 객체의 값을 하나씩 꺼내기 (현재 값 1개만 메모리에 유지)
result = (x for x in range(1, 4))
print(next(result))	 # 실행결과: 1
print(next(result))	 # 실행결과: 2
print(next(result))	 # 실행결과: 3