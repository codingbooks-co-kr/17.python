# ❷ * 연산자를 사용한 확장 언패킹 (여기서 * 연산자는 패킹으로 사용)

my_list = [1, 2, 3, 4, 5]	# 리스트 

*a, b, c = my_list		# 앞쪽 요소들을 리스트로 묶기
print(a, b, c)

a, *b, c = my_list		# 중간 요소들을 리스트로 묶기
print(a, b, c)

a, b, *c = my_list		# 뒤쪽 요소들을 리스트로 묶기
print(a, b, c)

*a, = my_list		# 모든 요소들을 리스트로 묶기
print(a)