num1 = (1, 2)			# 튜플1
num2 = (3, 4, 5)			# 튜플2

# * 연산자를 사용한 언패킹으로 튜플 병합
merged = (*num1, *num2)		# 튜플 병합
print(merged)

mixed = ('A', *num1, 'B', *num2)	# 요소 추가 튜플 병합
print(mixed)