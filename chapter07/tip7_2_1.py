part1 = "ABC"		# 문자열(str)
part2 = [1, 2]		# 리스트(list)
part3 = (3, 4)		# 튜플(tuple: [심화7.2])
part4 = {'B', 'C', 'D'}		# 세트(set: [심화8.2])

# 기존 방식 (각 자료형을 일일이 list()로 변환해서 더해야 함)
combined = list(part1) + part2 + [10, 20]
print(combined)

# 언패킹 병합 방식 (병합 후 리스트 생성, 직관적으로 추천)
combined = [*part1, *part2, 10, 20]
print(combined)

# 언패킹 병합 방식 (병합 후 튜플 생성)
combined = (*part1, *part2, *part3, *part4)
print(combined)	# 세트 포함 시 순서 보장 없음

# 언패킹 병합 방식 (병합 후 세트 생성)
combined = {*part1, *part2, *part3, *part4}
print(combined)	# 세트 생성 시 순서 보장 없고 중복 제거