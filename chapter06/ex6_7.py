word = "Python"		# 문자열

# ❶ 기본 언패킹: 문자열의 각 문자를 여러 변수에 차례로 할당
a, b, c, d, e, f = word	# 문자열 언패킹
print(a, b, c, d, e, f)

# ❷ * 연산자를 사용한 확장 언패킹 (여기서 * 연산자는 패킹으로 사용)
*a, b, c = word 		# 앞쪽 문자들을 리스트로 묶기
print(a, b, c)

a, *b, c = word 		# 중간의 문자들을 리스트로 묶기
print(a, b, c)

a, b, *c= word 		# 뒤쪽 문자들을 리스트로 묶기
print(a, b, c)

*a, = word 		# 모든 문자를 리스트로 묶기
print(a)

# ❸ _ 및 *_를 사용한 확장 언패킹 (여기서 * 연산자는 패킹으로 사용)
a, _, c, d, e, f = word 	# _에 할당된 문자를 무시
print(a, c, d, e, f)

a, _, _, _, e, f = word 	# 여러 _에 할당된 문자들을 무시
print(a, e, f)

*_, b, c, d = word 		# 앞쪽 문자들을 리스트로 묶어 무시
print(b, c, d)

_, b, *_, d = word 		# 중간의 문자들을 리스트로 묶어 무시
print(b, d)

a, _, c, *_ = word 		# 뒤쪽 문자들을 리스트로 묶어 무시
print(a, c)