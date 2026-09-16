# ❶ 시퀀스 병합: 서로 다른 자료형을 하나로 풀어서 묶기
result = [*"AB", *[1, 2], *(3, 4)] 
print(result)

# ❷ 시퀀스 병합: 서로 다른 자료형을 하나로 풀어서 묶기 
part1 = {1, 2}		# 세트
part2 = [2, 3, 4]		# 리스트
part3 = (4, 5)		# 튜플

result = [*part1, *part2, 4]
print(result)
result = {*part1, *part2, *part3}  # 순서 보장 없고 중복 요소 제거
print(result)