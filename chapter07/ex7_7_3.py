# ❸ _ 및 *_ 변수를 사용한 확장 언패킹 (여기서 * 연산자는 패킹으로 사용)

my_list = [1, 2, 3, 4, 5]	# 리스트 

a, _, c, d, e = my_list	# _에 할당된 요소를 무시
print(a, c, d, e)

_, _, _, d, e = my_list	# 여러 _에 할당된 요소들을 무시
print(d, e)

*_, d, e = my_list		# 앞쪽 요소들을 리스트로 묶어 무시
print(d, e)

a, b, *_, e = my_list	# 중간의 요소들을 리스트로 묶어 무시
print(a, b, e)

a, b, *_ = my_list		# 뒤쪽 요소들을 리스트로 묶어 무시
print(a, b)